export default defineNuxtConfig({
  compatibilityDate: '2025-09-12',
  devtools: { enabled: true },

  runtimeConfig: {
    public: {
      backendApiUrl: process.env.BACKEND_API_URL || 'http://localhost:8002',
    }
  },

  server: {
    port: 3000,
    host: 'localhost'
  }
})