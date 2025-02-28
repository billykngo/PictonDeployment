import path from "path";
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
      "@styles": path.resolve(__dirname, "src/styles"),
    },
    host: '0.0.0.0',  // Allows access from outside the container
    port: 8000,        // Match the port in your docker-compose.yml
    strictPort: true,  // Prevents Vite from switching ports automatically
  },
});
