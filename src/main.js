import {createApp} from 'vue'
import './style.css'
import App from './App.vue'
import Actions from "./components/Actions.vue";
import {createRouter, createWebHashHistory} from "vue-router";
import Home from "./components/Home.vue";
import Events from "./components/Events.vue";

const routes = [
    {path: '/', component: Home, name: "home"},
    {path: '/actions', component: Actions, name: "actions"},
    {path: '/events', component: Events, name: "events"},
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

createApp(App)
    .use(router)
    .mount('#app')
