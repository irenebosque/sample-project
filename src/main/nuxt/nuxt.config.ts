export default defineNuxtConfig({
  compatibilityDate: '2025-09-12',
  devtools: { enabled: true },
  ssr: true,

  runtimeConfig: {
    public: {
      backendApiUrl: process.env.BACKEND_API_URL || 'http://localhost:8000',
    }
  },

  server: {
    port: 3000,
    host: '0.0.0.0'
  }
})