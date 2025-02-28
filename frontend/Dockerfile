# Use an official Node.js image
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and lock file first (to use Docker caching)
COPY ["package.json", "pnpm-lock.yaml", "./"]

# Install dependencies inside the container
RUN npm install --global pnpm && pnpm install --frozen-lockfile

# Copy the rest of the frontend files (excluding node_modules via .dockerignore)
COPY . .

# Build the frontend
RUN npm run build

# Expose port 8000 for serving
EXPOSE 8000

# Start the Vite preview server
CMD ["npm", "run", "preview"]
