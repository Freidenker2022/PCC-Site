<template>
  <div class="q-pa-md">
    <img class="ico" src="../../public/from_site_logo.png">
    <h4 class="press">Bienvenido al sitio administrativo del PCC</h4>
    <div class="gutter-md" style="max-width: 300px">
      <q-file
        filled
        bottom-slots
        v-model="add_file"
        label="Label"
        counter
        max-files="12"
      >
        <template v-slot:append>
          <q-icon
            v-if="add_file !== null"
            name="close"
            @click.stop="add_file = null"
            class="cursor-pointer"
          />
        </template>

        <template v-slot:hint> Field hint </template>

        <template v-slot:after>
          <q-btn round dense flat icon="send" @click="post" />
        </template>
      </q-file>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";
import { Notify } from "quasar";

export default {
  setup() {
    const add_file = ref(null);
    const getFormData = (object) =>
      Object.keys(object).reduce((formData, key) => {
        formData.append(key, object[key]);
        return formData;
      }, new FormData());
    return {
      add_file,
      post() {
        let formData = new FormData();
        formData.append("file", add_file.value);
        const options = {
          headers: { "content-type": "multipart/form-data" },
        };
        // console.log(form_file);
        axios
          .post(
            "http://localhost:8000/api/upload-militant/",
            formData,
            options
          )
          .then((res) => {
            Notify.create({
              icon: "done",
              color: "positive",
              message: "Archivo procesado.",
            });
          })
          .catch((err) => {
            console.log(err.response);
            let error = err.request.statusText;
            // let msg = "";
            // for (let index = 0; index < errors.length; index++) {
            //   msg += errors[index];
            //   if (index !== msg.length - 1) msg += " ";
            // }
            Notify.create({
              icon: "error",
              color: "negative",
              message: "ERROR! El archivo no se puede procesar.",
            });
          });
      },
    };
  },
};
</script>

<style>
.ico{
  margin-left: 660px;
}
.press{
  margin-left: 400px;
}
.gutter-md{
  margin-left: 40%;
}
</style>
