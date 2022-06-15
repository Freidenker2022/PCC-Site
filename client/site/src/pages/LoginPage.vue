<template>
<meta name="Login">
  <div class="pa-md" style="max-width: 1000px">
    <img class="ico" src="../../public/from_site_logo.png" alt="" />
    <h5 class="mssg">Por favor inicia sesión ...</h5>
    <form
      @submit.prevent.stop="onSubmit"
      @reset.prevent.stop="onReset"
      class="gutter-md"
    >
      <q-input
        ref="nameRef"
        filled
        v-model="name"
        label="Usuario:"
        lazy-rules
        :rules="nameRules"
      />

      <q-input
        ref="passwordRef"
        filled
        type="password"
        v-model="password"
        label="Contraseña:"
        lazy-rules
        :rules="passwordRules"
      />

      <div>
        <q-btn label="Iniciar" type="submit" color="primary" />
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
import { useQuasar } from "quasar";
import { ref } from "vue";
import { useMeta } from "quasar";

const metadata = {
  title: 'PCC - Login',
  // meta: {
  //   description: {name: "PCC", content:"MilitantPage"}
  // }
}

export default {
  setup() {
    const $q = useQuasar();

    const name = ref(null);
    const nameRef = ref(null);

    const password = ref(null);
    const passwordRef = ref(null);

    return {
      meta: useMeta(metadata),
      name,
      nameRef,
      nameRules: [
        (val) => (val && val.length > 0) || "Por favor escribe tu nombre.",
      ],

      password,
      passwordRef,
      passwordRules: [
        (val) =>
          (val !== null && val !== "") || "Por favor escribe tu contraseña.",
      ],

      onSubmit() {
        nameRef.value.validate();
        passwordRef.value.validate();

        if (nameRef.value.hasError || passwordRef.value.hasError) {
          // form has error
        } else {
          $q.notify({
            icon: "done",
            color: "positive",
            message: "Submitted",
          });
        }
      },

      onReset() {
        name.value = null;
        password.value = null;

        nameRef.value.resetValidation();
        passwordRef.value.resetValidation();
      },
    };
  },
};
</script>

<style>
.gutter-md {
  margin-left: 45%;
  margin-top: 0em;
  display: block;
}
.ico {
  margin-left: 670px;
  margin-top: 3em;
}
.mssg {
  margin-left: 600px;
}
</style>
