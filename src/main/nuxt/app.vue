<template>
  <div>
    <h1>Random Word Generator</h1>
    <button @click="getRandomWord" :disabled="loading">
      {{ loading ? 'Loading...' : 'Get Random Word' }}
    </button>
    <div v-if="randomWord" style="margin-top: 20px; font-size: 24px; font-weight: bold;">
      {{ randomWord }}
    </div>
  </div>
</template>

<script setup>
const randomWord = ref('')
const loading = ref(false)

const getRandomWord = async () => {
  loading.value = true
  try {
    const data = await $fetch('/api/random-word')
    randomWord.value = data.word
  } catch (error) {
    console.error('Error fetching random word:', error)
    randomWord.value = 'Error getting word'
  } finally {
    loading.value = false
  }
}
</script>