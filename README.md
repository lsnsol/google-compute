# Google Cloud Compute Engine

##### _[Google Cloud Console](https://console.cloud.google.com)_

### Google Cloud Run

- Navigate to folder `cloud_run`.
- We have `main.py` and `requirements.txt` for running our flask server.
- Head to GCP and enable the `Cloud Run`
- Run the following command.

  ```sh
  cd cloud_run
  gcloud config set run/region asia-east1 
  gcloud run deploy --source . cr-api
  ```

### Google App Engine

- Navigate to folder `app_engine`.
- We have here an angular project, which can also be any other framework.
- Create an `app.yaml` file for configurations for the App Engine.
- In this `app.yml` file we will give basic configurations like `runtime, env, service, instance_class, handlers` etc.
- Runtime indicates the runtime environment of the App Engine - we will use `python39`.
- Runtime can be any of the following: **Go**, **Python**, **NodeJs**, **Java**, **PHP** or **Ruby**.
- env - stands for environment, we will use `standard`.
- service - is for the name of the service in app engine, we will name it `ae-fe`.
- instance_class - we will use as `F2`.
- handlers will have the urls for servicing we will specify as mentioned in `app.yaml`.
- Head to GCP and enable `App Engine`, follow the necessary steps and complete the process.
- Run the following commands.

  ```sh
  cd app_engine
  npm run build 
  gcloud app deploy
  ```

### Google Compute Engine (VM)

- Go to [Google Cloud Console](https://console.cloud.google.com)
- Create a project if not created
- Link a billing account
- Search for `VM` in the searchbar
- Enable the `VM` and follow necessary steps to complete it
- After setting up of VM open it via browser to access the OS installed on it to perform functions
- This is like a remote machine with internet connection and everything we run needs to be setup there to be used

## License

MIT
