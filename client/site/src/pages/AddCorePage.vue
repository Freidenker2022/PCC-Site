<template>
  <div class="q-pa-md">
    <img class="ico" src="../../public/from_site_logo.png" />
    <form
      @submit.prevent.stop="onSubmit"
      @reset.prevent.stop="onReset"
      class="q-gutter-md"
    >
      <q-input
        ref="codeRef"
        filled
        v-model="code"
        type="number"
        label="Código:"
        lazy-rules
        :rules="codeRules"
      />

      <q-input
        ref="nameRef"
        filled
        v-model="name"
        label="Nombre del Núcleo:"
        lazy-rules
        :rules="nameRules"
      />

      <q-select
      ref="provinceRef"
      filled v-model="province"
      :options="poptions"
      label="Provincia:"
      lazy-rules
      :rules="provinceRules"
      />

      <q-select
      ref="municipalityRef"
      filled v-model="municipality"
      :options="moptions"
      label="Municipio:"
      lazy-rules
      :rules="municipalityRules"
      />

      <q-input
        ref="districtRef"
        filled
        type="number"
        v-model="district"
        label="Distrito:"
        lazy-rules
        :rules="districtRules"
      />

      <q-input
        ref="political_areaRef"
        filled
        v-model="political_area"
        label="Area Política:"
        lazy-rules
        :rules="political_areaRules"
      />

      <q-input
        ref="sectorRef"
        filled
        v-model="sector"
        label="Sector:"
        lazy-rules
        :rules="sectorRules"
      />

      <q-input
        ref="subordinateRef"
        filled
        v-model="subordinate"
        label="Subordinado a:"
        lazy-rules
        :rules="subordinateRules"
      />

      <div class="btns">
        <q-btn
        label="Submit"
        type="submit"
        color="primary"
        />
        <q-btn
          label="Reset"
          type="reset"
          color="primary"
          flat
          class="q-ml-sm"
        />
      </div>
    </form>
  </div>
</template>

<script>
import { ref } from "vue";
import axios from "axios";
import { useQuasar } from "quasar";
import { Notify } from "quasar";
import { useMeta } from "quasar";

const metadata = {
  name: "PCC - Núcleo"
}

export default {
  methods:{
    select_mun_list() {
      this.moptions = {"Pinar del Río":["Pinar del Río", "San Juan y Martínez",
    "Sandino", "Los Palacios", "Guane", "La Palma", "Minas de Matahambre", "Mantua"],
    "La Habana":["Arroyo Naranjo", "Boyeros", "Centro Habana", "Cotorro", "Diez de Octubre",
    "El Cerro", "Guanabacoa", "La Habana del Este", "La Habana Vieja", "La Lisa", "Marianao",
    "Playa", "Plaza de la Revolución", "Regla", "San Miguel del Padrón"],
    "Artemisa":["Mariel", "Guanajay", "Caimito", "Bauta", "San Antonio de los Baños",
    "Güira de Melena", "Alquízar", "Artemisa", "Bahía Honda", "Candelaria", "San Cristóbal"],
    "Mayabeque":["Bejucal", "San José de las Lajas", "Jaruco", "Santa Cruz del Norte", "Madruga",
    "Nueva Paz", "San Nicolás de Bari", "Güines", "Melena del Sur", "Batabanó", "Quivicán"],
    "Matanzas":["Algorta", "Arcos de Canasí", "Jagüey Grande", "Jovellanos", "Martí", "Matanzas",
    "Calimete", "Cárdenas", "Ciénaga de Zapata", "Colón", "Limonar", "Los Arabos",
    "Pedro Betancourt", "Perico", "Unión de Reyes"],
    "Cienfuegos":["Abreus", "Aguada de Pasajeros", "Cienfuegos", "Cruces", "Cumanayagua",
    "Lajas", "Palmira", "Rodas"],
    "Sancti Spiritus":["Sancti Spíritus", "Trinidad", "Cabaiguán", "Yaguajay", "Jatibonico",
    "Taguasco", "Fomento", "La Sierpe"],
    "Villa Clara":["Caibarién", "Camajuaní", "Cifuentes", "Corralillo", "Encrucijada", "Manicaragua",
    "Placetas", "Quemado de Güines", "Ranchuelo", "Remedios", "Sagua la Grande", "Santa Clara", "Santo Domingo"],
    "Camagüey":["Camagüey", "Guáimaro", "Nuevitas", "Céspedes", "Jimaguayú", "Sibanicú", "Esmeralda",
    "Minas", "Sierra de Cubitas", "Florida", "Najasa", "Vertientes", "Santa Cruz del Sur"],
    "Holguín":["Antilla", "Báguanos", "Banes", "Cacocum", "Calixto García", "Cueto", "Frank País",
    "Gibara", "Holguín", "Mayarí", "Moa", "Rafael Freyre", "Sagua de Tánamo", "Urbano Noris"],
    "Guantánamo":["Baracoa", "Caimanera", "El Salvador", "Guantánamo", "Imías", "Maisí", "Manuel Tames",
    "Niceto Pérez", "San Antonio del Sur", "Yateras"],
    "Santiago de Cuba":["Contramaestre", 'Guamá', "Mella", 'Palma Soriano', "San Luis", "Santiago de Cuba",
    "Segundo Frente", "Songo-La Maya", "Tercer Frente"],
    "Granma":["Bartolomé Masó", "Bayamo", "Buey Arriba", "Campechuela", "Cauto Cristo", "Guisa",
    "Jiguaní", "Manzanillo", "Media Luna", "Niquero", "Pilón", "Río Cauto", "Yara"],
    "Isla de la Juventud":["Isla de la Juventud"]
    }[this.province.value];
    },
  },
  setup() {
    const q = useQuasar();

    const name = ref(null);
    const nameRef = ref(null);

    const code = ref(null);
    const codeRef = ref(null);

    const district = ref(null);
    const districtRef = ref(null);

    const sector = ref(null);
    const sectorRef = ref(null);

    const political_area = ref(null);
    const political_areaRef = ref(null);

    const subordinate = ref(null);
    const subordinateRef = ref(null);

    const municipality = ref(null);
    const moptions = ref(null);
    const municipalityRef = ref(null);

    const poptions = ref(null);
    const province = ref(null);
    const provinceRef = ref(null);
    const provinceRules = ref(null);

    return {
      meta: useMeta(metadata),
      code,
      codeRef,
      codeRules: [(val) => (val && val.length > 0 && val.length < 6) || "Please type something"],

      name,
      nameRef,
      nameRules: [(val) => (val && val.length > 0) || "Please type something"],

      district,
      districtRef,
      districtRules: [
        (val) => (val && val.length > 0) || "Please type something",
      ],

      political_area,
      political_areaRef,
      political_areaRules: [
        (val) => (val && val.length > 0) || "Please type something",
      ],

      sector,
      sectorRef,
      sectorRules: [
        (val) => (val && val.length > 0) || "Please type something",
      ],

      subordinate,
      subordinateRef,
      subordinateRules: [
        (val) => (val && val.length > 0) || "Please type something", select_mun_list()
      ],

      province,
      provinceRef,
      poptions: ['La Habana', "Pinar del Río", "Artemisa", 'Mayabeque',
      "Matanzas", "Cienfuegos", "Sancti Spiritus", "Villa Clara", "Camagüey", "Las Tunas",
      "Holguín", "Guantánamo", "Santiago de Cuba", "Granma", "Isla de la Juventud (municipio especial)"],
      provinceRules: [
        (val) => (val && val.length > 0) || "Please chose something",
      ],

      municipality,
      municipalityRef,
      moptions,
      municipalityRules: [
        (val) => (val && val.length > 0) || "Please type something",
      ],

      onSubmit() {
        nameRef.value.validate();
        codeRef.value.validate();
        sectorRef.value.validate();
        political_areaRef.value.validate();
        districtRef.value.validate();
        subordinateRef.value.validate();

        if (
          nameRef.value.hasError ||
          codeRef.value.hasError ||
          sectorRef.value.hasError ||
          provinceRef.value.hasError ||
          political_areaRef.value.hasError ||
          districtRef.value.hasError ||
          subordinateRef.value.hasError ||
          municipalityRef.value.hasError
        ) {
          Notify.create({
            icon: "error",
            color: "negative",
            message: "Faltan campos por rellenar.",
          });
          console.log();
        } else {
          try {
            axios
              .post("http://localhost:8000/api/core/", {
                code: this.code,
                name: this.name,
                sector: this.sector,
                political_area: this.political_area,
                district: this.district,
                subordinate: this.subordinate,
                municipality: this.municipality,
                province: this.province,
              })
              .then((res) => {
                Notify.create({
                  icon: "done",
                  color: "positive",
                  message: "Núcleo creado.",
                });
                window.open("./core");
                window.close();
              })
              .catch((err) => {
                let errors = err.response.data.code;
                let msg = "";
                for (let index = 0; index < errors.length; index++) {
                  msg += errors[index];
                  if (index !== msg.length - 1) msg += " ";
                }
                Notify.create({
                  icon: "error",
                  color: "negative",
                  message: msg,
                });
              });
          } catch (err) {}
        }
      },

      onReset() {
        this.code = null;
        this.name = null;
        this.sector = null;
        this.political_area = null;
        this.district = null;
        this.subordinate = null;
        this.province = null;
        this.municipality = null;

        nameRef.value.resetValidation();
        codeRef.value.resetValidation();
        sectorRef.value.resetValidation();
        provinceRef.value.resetValidation();
        municipality.value.resetValidation();
        political_areaRef.value.resetValidation();
        districtRef.value.resetValidation();
        subordinateRef.value.resetValidation();
      },
    };
  },
};
</script>

<style>
.q-gutter-md {
  margin-left: 45%;
  margin-top: 1em;
}
.ico {
  margin-left: 660px;
}
.q-pa-md {
  max-height: 1000px;
  max-width: 1000px;
}

.q-input {
  margin-top: 5px;
}
.btns {
  margin-top: 2px;
}
</style>
