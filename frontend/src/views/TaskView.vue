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

                    <v-divider class="my-6">

                    </v-divider>

                    <v-card-title class="text-h5">タスク一覧</v-card-title>
                    <v-alert v-if="taskList.length === 0" type="info" class="mx-4 my-2">
                        登録されたタスクはありません。
                    </v-alert>

                    <v-row>
                        <v-col
                        v-for="task in taskList"
                        :key="task.id"
                        cols="12"
                        md="6"
                        >
                        <v-card variant="outlined" class="mb-2">
                            <v-card-item>
                                <div>
                                    <div
                                    class="text-overline mb-1">
                                    分類:{{ task.task_index === 'business_task_task' ? '業務タスク' : '日常タスク' }}
                                     優先度:{{ task.priority }}
                                    </div>
                                    <div class="text-h6 mb-1">{{ task.task_title }}</div>
                                    <div class="text-caption text-medium-emphasis">締め切り:{{ task.deadline }}</div>
                                </div>
                            </v-card-item>
                            <v-card-text v-if="task.task_description">
                                {{ task.task_description }}
                            </v-card-text>
                        </v-card>
                        </v-col>
                    </v-row>
                </v-card-text>
            </v-card>
        </v-container>
</template>

<script setup lang="ts">
import { ref , onMounted} from 'vue';
import axios from 'axios';

const taskForm = ref({
    user_id:'user_1',
    task_index:'business_task_task',
    deadline:'',
    priority:1,
    task_title:'テストタイトル',
    task_description:''

});

const taskList =ref<any[]>([]);

const fetchTasks= async () =>{
    try{
        const response = await axios.get('http://127.0.0.1:8000/api/tasks')
        taskList.value =response.data;
        console.log('取得したタスク一覧' ,response.data);
    }catch (error) {
        console.error('タスク一覧を取得失敗しました。' , error);
    }
};

onMounted(() =>{
    fetchTasks();
});


const submitTask = async () =>{
    try {
        
        console.log('送信するタスクデータ:', taskForm.value);
        const response = await axios.post('http://127.0.0.1:8000/api/tasks', taskForm.value);
        taskList.value = response.data;
        console.log('APIのレスポンス:', response.data);
        alert('タスクが正常に送信されました！');
    }catch (error){
        console.error('タスク送信中にエラーが発生:', error);
        alert('送信失敗。FastAPIが起動しているか確認してください。')
    }
};


</script>