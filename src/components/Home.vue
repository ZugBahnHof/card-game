<template>
  <div>
    <h1>Card game</h1>
    <p>Choose your view:</p>
    <div>
      <router-link to="actions">Actions</router-link>
      <router-link to="events">Events</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home"
}
</script>

<style scoped>

</style>