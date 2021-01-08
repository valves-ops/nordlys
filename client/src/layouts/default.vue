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
            <v-img
                v-bind="props"
                gradient="to bottom, rgba(0,0,0,0), rgba(0,0,0,1)"
            ></v-img>
        </template>
        <v-row>
            <v-col cols="3"> </v-col>
            <v-col class="d-flex justify-space-around">
                <v-toolbar-title class="justify-center"
                    >NORDLYS</v-toolbar-title
                ></v-col
            >
            <v-col cols="3" class="d-flex justify-end">
                <v-btn icon>
                    <v-icon>mdi-help-circle</v-icon>
                </v-btn>

                <v-btn icon>
                    <v-icon>mdi-cog</v-icon>
                </v-btn></v-col
            >
        </v-row>
        <!-- <v-spacer></v-spacer>
        <v-toolbar-title class="justify-center">NORDLYS</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon>
            <v-icon>mdi-help-circle</v-icon>
        </v-btn>

        <v-btn icon>
            <v-icon>mdi-cog</v-icon>
        </v-btn> -->

        <template v-slot:extension>
            <v-tabs fixed-tabs>
                <v-tab>Effects</v-tab>
                <v-tab>Dash</v-tab>
                <v-tab>Configs</v-tab>
            </v-tabs>
        </template>
    </v-app-bar>
</template>

<script>
export default {}
</script>

<style scoped></style>
