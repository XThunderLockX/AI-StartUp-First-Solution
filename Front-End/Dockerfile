FROM node:20-alpine

WORKDIR /frontend

# Install deps if package.json exists
COPY package*.json* ./
RUN if [ -f "package.json" ]; then npm ci || npm install; fi

# Copy the rest of the app (dev bind mount will override in compose)
COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]

