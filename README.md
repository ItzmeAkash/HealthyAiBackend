# Nutripalate.AI❤️‍🩹

## 🚀Introducing **Nutripalate.Ai**
##### Revolutionize your wellness journey with Nutripalate AI - your AI-powered partner for healthy living. Seamlessly integrating into your lifestyle, it offers personalized diet recommendations, serves as your cooking assistant, and effortlessly detects food images to provide detailed nutritional insights. Embrace a healthier you with Nutripalate AI by your side 🍽️


## 🚀Services 🍴

##### 🍎 **Diet Recommendation** :- Say goodbye👋🏻 to generic diet plans!📝 Nutripalate AI utilizes advanced AI algorithms to deliver personalized diet recommendations tailored to each user's unique health goals. It delivers each meal with five foods each

##### 🍜 **Recipe Generator** :- Never run out of healthy meal ideas again! 🍝 With Nutripalate AI recipe generator, users can discover an endless array of delicious and nutritious recipes based on their available ingredients and dietary restrictions


##### 📸 **Food Images Classifications** :- Make informed food choices effortlessly! 😋 Nutripalate AI accurately classifies food images, providing users with valuable insights to support their healthy eating habits


## How to run locally 🛠️
   - Before the following steps make sure you have [git](https://git-scm.com/download), [Anaconda](https://www.anaconda.com/) or [Vscode](https://code.visualstudio.com/) installed on your system

   - Clone the complete project with `git clone https://github.com/ItzmeAkash/HealthyAiBackend` or you can just download the code and unzip it 

   - **Note:** The master branch doesn't have the updated code used for deployment, to download the updated code used for deployment you can use the following command
  ```
  ❯ git clone -b deploy https://github.com/ItzmeAkash/HealthyAiBackend/
  ```
- `deploy` branch has only the code required for deploying the app 
- It is highly recommended to clone the deploy branch for running the project locally (the further steps apply only if you have the deploy branch cloned)
- Once the project is cloned, open anaconda prompt or CMD in the directory where the project was cloned and paste the following block


```bash
# To Create the environment
conda create -n healthyai python=3.10.13 -y
```

```bash
# To install all the requirements
pip install -r requirements.txt
```

```bash
# migrate the database
python manage.py makemigrations
python manage.py migrate
```

```bash
#Finally, run the project with
python manage.py runserver
```
- Open the localhost url provided after running `http://localhost:8000/` and now you can use the project locally in your web browser.



### Frontend Web Application🌐
##### Hosted On vercel [Nutripalate.AI](https://nutripalate.vercel.app/)
##### GitHub Repo [Nutripalate.AI](https://github.com/ItzmeAkash/HeathyAiFrontend)

## License 📝
This project is licensed under [ Apache-2.0 License](https://github.com/ItzmeAkash/HealthyAiBackend?tab=Apache-2.0-1-ov-file).

## Contact 📞

#### If you have any doubt or want to contribute feel free to email me or hit me up on [LinkedIn](www.linkedin.com/in/itzmeakash)











