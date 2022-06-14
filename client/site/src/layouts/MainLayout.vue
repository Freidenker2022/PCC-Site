<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="toggleLeftDrawer" />

        <q-toolbar-title>
          <q-avatar>
            <img src="../../public/from_site_logo.png" />
          </q-avatar>
          Sitio Administrativo UH PCC
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      side="left"
      overlay
      behavior="desktop"
      elevated
    >
      <div class="q-pa-md" style="max-width: 350px">
        <q-list bordered separator>
          <q-item clickable v-ripple>
            <q-item-section>
              <a href="/home">
                <q-item-label overline>PAGINA PRINCIPAL</q-item-label>
                <q-item-label>Item with caption</q-item-label>
              </a>
            </q-item-section>
          </q-item>
          <q-item clickable v-ripple>
            <q-item-section>
              <a href="/militant">
                <q-item-label overline>MILITANTES</q-item-label>
                <q-item-label>Item with caption</q-item-label>
              </a>
            </q-item-section>
          </q-item>
          <q-item clickable v-ripple>
            <q-item-section>
              <a href="/debt">
                <q-item-label overline>ATRASOS</q-item-label>
                <q-item-label>Item with caption</q-item-label>
              </a>
            </q-item-section>
          </q-item>
          <q-item clickable v-ripple>
            <q-item-section>
              <a href="/core">
                <q-item-label overline>NUCLEOS</q-item-label>
                <q-item-label>Item with caption</q-item-label>
              </a>
            </q-item-section>
          </q-item>
        </q-list>
      </div>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "MainLayout",
  setup() {
    const leftDrawerOpen = ref(false);

    return {
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
    };
  },
});
</script>

<style>
a:link {
  color: #1976d2;
  text-decoration: none;
}

a:visited {
  color: #1976d2;
  text-decoration: none;
}

a:hover {
  color: #1976d2;
  text-decoration: none;
}

a:active {
  color: #1976d2;
  text-decoration: none;
}
</style>
