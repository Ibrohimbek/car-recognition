# Backend service

The service stores and supplies endpoints to recognize cars model by photo. 
Used Fastai framework to train a model.



## Codebase

The project folders description:

- deployment: this is where deployment related stuff is stored.
- recognition: this is where the main code is stored
    - api: this is where all the API is stored
    - domain: this is where all domain business logic stored
    - contrib: this is where util functions/classes are stored
    - models: this is where framework models are stored
    - settings: well, settings
- tests: this is where the tests are stored.
- requirements: required packages list


## Getting Started

Take and run. :)

## Tests

Pytest is used for writing and running the tests. 
As the project is running inside a docker container, tests should be run from the container:

```bash
docker-compose exec car-recognition pytest
```
