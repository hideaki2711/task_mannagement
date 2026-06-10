

import HomeView from './views/HomeView.vue';
import TaskView from './views/TaskView.vue';
import { createRouter , createWebHistory } from 'vue-router';

const routes = [
    {
        path:"/",
        name:"home",
        component:HomeView
    },
    {
        path:'/task',
        name:'task',
        component:TaskView,
    }

]

const router = createRouter ({
    history:createWebHistory(),
    routes,  
});

export default router;