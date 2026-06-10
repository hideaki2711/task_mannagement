<template>
<v-conteiner class="fill-height" fluid>
    <v-row align="center" justify="center">
        <v-col size="64" sm="8" md="6" class="text-center">
            <v-icon size="64" color="primary" class="mb-4"> </v-icon>
                <h1 class="text-h3 font-weight-bold mb-3 text-grey-darken-3">Task_managment-app
                </h1>
                <p class="text-subtitle-1 text-medium-emphasis mb-6">
                    vue3とpython＋SQLiteを使用して、開発した<br>
                    一気通貫型のタスク管理システムです。
                </p>
                <v-divider class="my-6"></v-divider>
                <v-row class="mb-6  text-left">
                    <v-col cols="12" sm="6">
                        <v-card variant="flat" class="bg-blue-lighten-5 pa-3">
                            <v-card-title class="text-subtitle-1 font-weight-bould">
                                <v-icon color="primary" class="mr-2" >mid-server</v-icon>モダンなAPI通信
                            </v-card-title>
                            <v-card-text class="text-caption">FastAPIとSQLiteを接続し、データの永続化を実現。</v-card-text>
                        </v-card>
                    </v-col>
                    <v-col cols="12" sm="6">
                        <v-card variant="flat" class="bg-green-lighten-5 pa-3">
                            <v-card-title class="text-subtitle-1 font-weight-bould">
                                <v-icon color="sucsess" class="mr-2">mdi-flash</v-icon>高速でリアルタイム検索
                            </v-card-title>
                            <v-card-text class="text-caption">JavaScriptの算出したプロパティを活用して、画面リロードを無しで絞りこみ</v-card-text>
                        </v-card>
                    </v-col>
                </v-row>
                            <v-btn
                        color="primary"
                        size="x-large"
                        rounded="xl"
                        elevertion="2"
                        to="/task"
                        prepend-icon="mdi-arrow-right-circle"
                        >アプリ開始（タスク管理画面へ）
                        </v-btn>

               </v-col>
          </v-row>
    </v-conteiner>
</template>

<script setup lang="ts"></script>