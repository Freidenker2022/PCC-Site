<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md">
      <center><h4 style="color: #1a1b20">ATRASOS</h4></center>
      <q-table
        class="my-sticky-header-column-table"
        :rows="rows"
        :columns="columns"
        row-key="ci"
        :filter="filter"
        :separator="separator"
        selection="single"
        v-model:selected="selected"
      >
        <template v-slot:top>
          <q-input
            borderless
            dense
            debounce="300"
            color="primary"
            v-model="filter"
          >
            <template v-slot:append>
              <q-icon name="search" />
            </template>
          </q-input>
        </template>
      </q-table>
    </div>
    <div class="q-mt-md"></div>
  </q-page>
</template>
<script>
import { defineComponent } from "vue";
import { ref } from "vue";
import axios from "src/boot/axios";

const columns = [
  {
    name: "ci",
    label: "No. Identidad",
    align: "left",
    field: "ci",
    sortable: true,
  },
  {
    name: "militant_name",
    align: "center",
    label: "Nombre",
    field: "name",
    sortable: true,
  },
  {
    name: "first_lastname",
    align: "center",
    label: "Primer Apellido",
    field: "first_lastname",
    sortable: true,
  },
  {
    name: "second_lastname",
    align: "center",
    label: "Segundo Apellido",
    field: "second_lastname",
    sortable: true,
  },
  {
    name: "debts",
    align: "center",
    label: "Atrasos",
    field: "debts",
    sortable: true,
  },
];

export default defineComponent({
  name: "DebtsPage",
  data() {
    return {
      selected: ref([]),
      columns,
      loading: ref(false),
      filter: ref(""),
      rowCount: ref(10),
      rows: [],
      separator: ref("cell"),
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      this.$axios
        .get("http://localhost:8000/pcc/debts/")
        .then((res) => {
          this.rows = res.data;
          this.rows = this.giveFormat(this.rows);
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    giveFormat(post) {
      let result = "";
      for (let mil = 0; mil < post.length; mil++) {
        let debts = post[mil]["debts"];
        result =
          "Atraso más antiguo: mes: " +
          debts[0]["month"] +
          " año: " +
          debts[0]["year"] +
          " ";
        let not_declared = "";
        let payable_sum = 0;
        let paid = 0;
        for (let index = 0; index < debts.length; index++) {
          if (debts["amount_payable"] == null)
            not_declared = ". Hay fechas sin salario declarado.";
          else {
            payable_sum += debts["amount_payable"];
            paid += debts["amount_paid"];
          }
        }
        result += ". Total: " + (payable_sum - paid);
        result += not_declared;
        post[mil].debts = result;
      }
      return post;
    },
  },
  created() {
    this.getData();
  },
});
</script>

<style lang="sass">
.q-checkbox__inner
  color: $accent

.text-grey-8
  color: $accent

.my-sticky-header-column-table
  /* height or max-height is important */
  max-height: 500px

  /* specifying max-width so the example can
    highlight the sticky column on any browser window */
  max-width: 100%

  td:first-child
    /* bg color is important for td; just specify one */
    background-color: $secondary !important

  tr th
    position: sticky
    /* higher than z-index for td below */
    z-index: 2
    /* bg color is important; just specify one */
    background: $primary
    color: #fff

  /* this will be the loading indicator */
  thead tr:last-child th
    /* height of all previous header rows */
    top: 48px
    /* highest z-index */
    z-index: 3
  thead tr:first-child th
    top: 0
    z-index: 1
  tr:first-child th:first-child
    /* highest z-index */
    z-index: 3

  td:first-child
    z-index: 1

  td:first-child, th:first-child
    position: sticky
    left: 0
</style>
