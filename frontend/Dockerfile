# Use official Node.js image
FROM node:18-alpine

# Set working directory inside container
WORKDIR /app

# Copy package.json and lock file
COPY package.json pnpm-lock.yaml ./

# Install dependencies using pnpm
RUN npm install --global pnpm && pnpm install

# Copy the rest of the project files
COPY . .

# Build the project for production
RUN npm run build

# Expose the port Vite will use
EXPOSE 8000

# Start the production server
CMD ["npm", "run", "preview"]
