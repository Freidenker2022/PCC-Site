<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md">
      <h4 class="core" style="color: #1a1b20">NUCLEOS</h4>
      <q-table
        class="my-sticky-header-column-table"
        :rows="rows"
        :columns="columns"
        row-key="code"
        :filter="filter"
        selection="single"
        v-model:selected="selected"
        :separator="separator"
      >
        <template v-slot:top>
          <q-btn
            class="add"
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
import axios from "axios";
import { useMeta } from "quasar";

const columns = [
  {
    name: "code",
    label: "No. Núcleo",
    align: "left",
    field: "code",
    format: (val) => `${val}`,
    sortable: true,
  },
  {
    name: "name",
    align: "center",
    label: "Nombre",
    field: "name",
    sortable: true,
  },
  {
    name: "district",
    align: "center",
    label: "Distrito",
    field: "district",
    sortable: true,
  },
  {
    name: "political_area",
    align: "center",
    label: "Area Política",
    field: "political_area",
    sortable: true,
  },
  {
    name: "sector",
    align: "center",
    label: "Sector",
    field: "sector",
    sortable: true,
  },
  {
    name: "subordinate",
    align: "center",
    label: "Subordinado",
    field: "subordinate",
    sortable: true,
  },
];
const metadata = {
  title: 'PCC - Núcleos',
  meta: {
    description: {name: "Militantes", content:"MilitantPage"}
  }
}
const selected = ref([]);
export default defineComponent({
  name: "MilitantsPage",
  data() {
    return {
      meta: useMeta(metadata),
      selected,
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
        .get("http://localhost:8000/api/core/")
        .then((res) => {
          this.rows = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    reloadPage() {
      window.location.reload();
    },
    addRow() {
      window.open("./addcore");
      window.close();
    },
    removeRow() {
      this.$axios.delete(
        "http://localhost:8000/api/core/" + this.selected[0].code + "/"
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
.core
  margin-left: 400px
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
