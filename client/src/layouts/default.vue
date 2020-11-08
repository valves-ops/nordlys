<template>
    <v-app-bar
        absolute
        color="#fcb69f"
        dark
        shrink-on-scroll
        src="https://i.imgur.com/FCHP7CN.jpg"
        scroll-target="#scrolling-techniques-2"
    >
        <template v-slot:img="{ props }">
            <v-img v-bind="props"></v-img>
        </template>

        <v-app-bar-nav-icon></v-app-bar-nav-icon>

        <v-toolbar-title>Hot Reload</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn icon>
            <v-icon>mdi-chevron-down</v-icon>
        </v-btn>

        <v-btn icon>
            <v-icon>mdi-heart</v-icon>
        </v-btn>

        <v-btn icon>
            <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>
    </v-app-bar>
</template>

<script>
export default {}
</script>

<style scoped></style>
