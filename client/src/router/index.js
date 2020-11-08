import Vue from 'vue'
import Router from 'vue-router'
import Container from '../layouts/default.vue'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            component: Container,
        },
    ],
    mode: 'history',
})
