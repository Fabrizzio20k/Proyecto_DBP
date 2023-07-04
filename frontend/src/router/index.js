import { createRouter, createWebHistory } from "vue-router";
import IndexView from "../views/IndexView.vue";
import LoginView from "../views/LoginView.vue";
import LogoutView from "../views/LogoutView.vue";
import NewUserView from "../views/NewUserView.vue";
import RecoverUserView from "../views/RecoverUserView.vue";
import ProfileView from "../views/ProfileView.vue";
import SearchView from "../views/SearchView.vue";
import VideogameView from "../views/VideogameView.vue";
import CheckoutView from "../views/CheckoutView.vue";
import ResumePurchaseView from "../views/ResumePurchaseView.vue";

const routes = [
  {
    path: "/",
    name: "index",
    meta: { title: "Compra los mejores juegos aquí" },
    component: IndexView,
  },
  {
    path: "/login",
    name: "login",
    meta: { title: "Inicia aquí y ahora" },
    component: LoginView,
  },
  {
    path: "/logout",
    name: "logout",
    meta: { title: "Esperamos verte pronto :)" },
    component: LogoutView,
  },
  {
    path: "/new_user",
    name: "new_user",
    meta: { title: "Unete a esta gran experiencia" },
    component: NewUserView,
  },
  {
    path: "/password_recovery",
    name: "password_recovery",
    meta: { title: "Recupere su contraseña" },
    component: RecoverUserView,
  },
  {
    path: "/profile",
    name: "profile",
    meta: { title: "Perfil del usuario" },
    component: ProfileView,
  },
  {
    path: "/search",
    name: "search",
    meta: { title: "Resultados de la busqueda" },
    component: SearchView,
  },
  {
    path: "/videogame",
    name: "videogame",
    meta: { title: "Detalles del videojuego" },
    component: VideogameView,
  },
  {
    path: "/checkout",
    name: "checkout",
    meta: { title: "Compra casi lista..." },
    component: CheckoutView,
  },
  {
    path: "/resume",
    name: "resume",
    meta: { title: "Gracias por su compra" },
    component: ResumePurchaseView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  next();
});

export default router;
