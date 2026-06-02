<template>
        <v-container>
            <v-card>
                <v-card-title>
                    タスク入力画面
                </v-card-title>
                <v-card-text>

                <v-form @submit.prevent="submitTask">
                
                <v-select
                    v-model="taskForm.user_id"
                    :items="['user_1','user_2']"
                    label="ログインユーザー（デバック用切り替え）"
                    required
                ></v-select>

                <v-select
                    v-model="taskForm.task_index"
                    :items="[
                        { title:'日常タスク', value:'regular_task'},
                        { title:'業務タスク', value:'business_task_task'}
                    ]"
                    item-title="title"
                    item-value="value"
                    label="タスクの種類"
                    required
                ></v-select>

                <v-text-field
                    v-model="taskForm.deadline"
                    label="締め切り日付(例:2026-06-01)"
                    type="date"
                    required
                ></v-text-field>

                <v-slider
                    v-model="taskForm.priority"
                    min="1"
                    max="5"
                    step="1"
                    thumb-label="always"
                    label="優先順位（1低－5高）"
                    class="mt-4"
                ></v-slider>
                
                <v-text-field
                    v-model="taskForm.task_title"
                    label="タスクのタイトル*"
                    required
                ></v-text-field>
                
                <v-textarea
                    v-model="taskForm.task_description"
                    label="タスクの内容"
                    row="3"
                ></v-textarea>

                <v-btn type="submit" color="success" block size="large" class="mt-4"
                    >APIに送信
                </v-btn>

                    </v-form>
                </v-card-text>
            </v-card>
        </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

const taskForm = ref({
    user_id:'user_1',
    task_index:'business_task_task',
    deadline:'',
    priority:1,
    task_title:'テストタイトル',
    task_description:''

});

const submitTask = async () =>{
    try {
        
        console.log('送信するタスクデータ:', taskForm.value);
        const response = await axios.post('http://127.0.0.1:8000/api/tasks', taskForm.value);
        
        console.log('APIのレスポンス:', response.data);
        alert('タスクが正常に送信されました！');
    }catch (error){
        console.error('タスク送信中にエラーが発生:', error);
        alert('送信失敗。FastAPIが起動しているか確認してください。')
    }
};


</script>