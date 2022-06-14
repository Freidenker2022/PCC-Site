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

      <q-input
        ref="provinceRef"
        filled
        v-model="province"
        label="Provincia:"
        lazy-rules
        :rules="provinceRules"
      />

      <q-input
        ref="municipalityRef"
        filled
        v-model="municipality"
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
        <q-btn label="Submit" type="submit" color="primary" />
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

export default {
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
    const municipalityRef = ref(null);

    const province = ref(null);
    const provinceRef = ref(null);

    return {
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
        (val) => (val && val.length > 0) || "Please type something",
      ],

      province,
      provinceRef,
      provinceRules: [
        (val) => (val && val.length > 0) || "Please type something",
      ],

      municipality,
      municipalityRef,
      municipalityRules: [
        (val) => (val && val.length > 0) || "Please type something",
      ],

      submit() {},

      onSubmit() {
        nameRef.value.validate();
        codeRef.value.validate();
        provinceRef.value.validate();
        sectorRef.value.validate();
        political_areaRef.value.validate();
        districtRef.value.validate();
        subordinateRef.value.validate();
        municipalityRef.value.validate();

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
        code = null;
        name = null;
        sector = null;
        political_area = null;
        district = null;
        subordinate = null;
        province = null;
        municipality = null;

        nameRef.value.resetValidation();
        codeRef.value.resetValidation();
        provinceRef.value.resetValidation();
        sectorRef.value.resetValidation();
        political_areaRef.value.resetValidation();
        districtRef.value.resetValidation();
        subordinateRef.value.resetValidation();
        municipalityRef.value.resetValidation();
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
