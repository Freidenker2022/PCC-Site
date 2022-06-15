const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "/", component: () => import("pages/LoginPage.vue") },
      { path: "/militant", component: () => import("pages/MilitantPage.vue") },
      { path: "/debt", component: () => import("pages/DebtPage.vue") },
      { path: "/core", component: () => import("pages/CorePage.vue") },
      { path: "/addcore", component: () => import("pages/AddCorePage.vue") },
      { path: "/home", component: () => import("pages/HomePage.vue") },
      { path: "/test", component: () => import("pages/TestPage.vue") },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
