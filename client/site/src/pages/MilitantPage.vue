<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md">
      <center><h4 style="color: #1a1b20">MILITANTES</h4></center>
      <q-table
        class="my-sticky-header-column-table"
        :rows="rows"
        :columns="columns"
        row-key="ci"
        :filter="filter"
        selection="single"
        v-model:selected="selected"
        :separator="separator"
      >
        <template v-slot:top>
          <q-btn
            color="primary"
            :disable="loading"
            label="Agregar"
            @click="addRow"
          />
          <q-btn
            class="q-ml-sm"
            color="primary"
            :disable="loading"
            label="Eliminar"
            @click="removeRow"
          />
          <q-btn
            class="q-ml-sm"
            color="primary"
            :disable="loading"
            label="Modificar"
            @click="modifyRow"
          />
          <q-space />
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
];
export default defineComponent({
  name: "MilitantsPage",
  data() {
    return {
      selected: ref([]),
      columns,
      rows: [],
      loading: ref(false),
      filter: ref(""),
      rowCount: ref(10),
      separator: ref("cell"),
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      this.$axios
        .get("http://localhost:8000/api/militant/")
        .then((res) => {
          this.rows = res.data;
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    addRow() {},
    removeRow() {
      this.$axios.delete(
        "http://localhost:8000/api/militant/" + this.selected[0].ci + "/"
      );
      window.location.reload();
    },
    modifyRow() {},
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
