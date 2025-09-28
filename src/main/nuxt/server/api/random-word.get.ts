export default defineEventHandler(async (event) => {
  try {
    const { public: { backendApiUrl } } = useRuntimeConfig(event)

    const response = await $fetch(`${backendApiUrl}/api/random-word`)

    return {
      success: true,
      word: response.word
    }
  } catch (error) {
    console.error('Error getting random word from backend:', error)
    return {
      success: false,
      error: error.message
    }
  }
})