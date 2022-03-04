## Microservices task-1

### Prerequisites
* Docker CLI tools

### Run demo
from root directory:
* run all microservices:
```bash
docker-compose -f docker/docker-compose.yml up
```

* run each microservice separately:
```bash
docker compose -f docker/docker-compose.yml up facade_service/logging_service/messages_service
```

### Example demo
![example](/res/demo.gif)
