<meta name="google-site-verification" content="rn3x0ynUYDEKwcYUpAojekHXi0ZQPEG2psZrYf9Ylgo" />


 ## <div align="center"><img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/cd085b32-5d66-4016-b691-272b6631c8b0" /> Construct 3 Cordova ZIP to APK Builder 
   <div align="center"><img width="200" height="200" alt="" src="https://github.com/user-attachments/assets/b427cf12-2630-4aff-8d52-a465ac1397cf" />
<br>
<br>
      
![GitHub release (latest by date)](https://img.shields.io/github/v/release/EwenLoy/Saturn-Builder)
![GitHub downloads](https://img.shields.io/github/downloads/EwenLoy/Saturn-Builder/total)
![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-blue)


<div align="left">
   
## 📖 What is Saturn-Builder? / Что это?
<div align="left"> Saturn-Builder is a friendly app made with Python that helps you build Android apps without complicated setup. It downloads and installs everything you need (like special tools) on its own. Whether you're new to app-making or have some experience, this tool makes it simple to create your own apps for Android!
<br>
<br>
<div align="left"> Saturn-Builder - это удобное приложение, которое поможет вам создавать приложения для Android без сложной настройки. Оно самостоятельно загружает и устанавливает все, что вам нужно (например, специальные инструменты). Независимо от того, новичок вы в создании приложений или у вас есть некоторый опыт, этот инструмент упрощает создание ваших собственных приложений для Android!

## 🌟 What Can It Do? / Возможности

| Feature                  | What It Means                                    |
|--------------------------|--------------------------------------------------|
| 🛠️ **Easy Setup**        | Automatically installs tools you need (~1 GB).   |
| 📱 **Make Apps**          | Creates APK or AAB files for your Android apps.  |
| 🌐 **Language Switch**    | Change the app’s language to English or Russian. |
| 📜 **Show Progress**      | Shows you what’s happening while building.       |
| 🖥️ **Simple Interface**   | Easy-to-use screen to control everything.        |

## 🛠️ How to Get Started / Как начать

Saturn-Builder works on **Windows 10 or 11**. / Работает на win 10, 11 (windows 7 не пробовал, попробуйте если хотите)

1. Visit the [releases page](https://github.com/EwenLoy/Saturn-Builder/releases/) / Просто скачайте exe со страницы релизов
2. Download the `Saturn-Builder.exe`.
3. Double-click the file to install and open the app.
4. If you don't want to read the instructions, you can watch the [video guide](https://youtu.be/iGbkVkpYeIA) / Если вы не хотите читать инструкции, вы можете посмотреть [гайд на YouTube](https://youtu.be/F3EWrLdfKYM)
## 👀 How to use / Как пользоваться

1. **First start**: / Первый запуск
   - After installing, click `Saturn-Builder.exe` to start.
   - The first time, it will ask to install some tools. Click  **install dependencies** to get started, or `Skip for Now` if you want to try it later (but you won’t be able to make apps yet).
   - При первом запуске вам будет предложено установить необходимые зависимости (~1GB), однако если вы откажетесь, приложение не будет работать
    <br>

   > **🚨 Важный момент! Saturn-Builder.exe должен быть в английской папке!
   > При использовании в названии папок русских символов ничего работать не будет!**
   
   > "D:\FOLDER\SaturnBuilder_1.0.exe" ✅
   
   > "D:\пака на русском\SaturnBuilder_1.0.exe" ❌
   
1. **Pick a Language after installing dependencies**: / выберите язык интерфейса (если по англ не понимаете)
   - Choose English or Russian from a dropdown menu in the app.
   - The app will change its language right away!

2. **Load Cordova Project (zip) / Android Studio Project / HTML5 Project**: / нажмите кнопку загрузить проект (Load project) ваш zip архив Cordova
3. **Choose build type** / Выберете тип сборки
- Debug APK
- Unsigned release APK
- Unsigned Android App Bundle
- Signed debug APK
- Signed release APK
- Signed Android App Bundle
4. **Build Your App**: / Сборка вашего приложения
   - If you need a special key for your app, follow the steps to add it / Если подписанная сборка, подгрузите или создайте ключи
   - Click **Build** and watch the progress on the screen / Нажмите "Собрать" и ожидайте

5. **Get Your App**: / Получите ваше приложение
   - When it’s done, your app files (APK or AAB) will be in your project folder, and the folder will open so you can see them!
   - Когда сборка закончится, откроется проводник с вашим файлом

## 🚨Possible problems / Возможные проблемы
 **Убедитесь, что у вас НЕ ИСПОЛЬЗУЕТСЯ КИРИЛЛИЦА (РУС БУКВЫ) в проекте! Иначе получите ошибку:**
 
**Make sure that you DO NOT USE CYRILLIC LETTERS in your project! Otherwise you will get an error:**
>[19:06:24] ❌ Command finished with code 1 <br><br>
>[19:06:24] ❌ Error: Cordova build failed with code 1 <br><br>
>[19:06:24] Traceback (most recent call last): <br><br>
> Exception: Cordova build failed with code 1 <br><br>

✅ Solution: rename all files and names to English, including icons <br>
✅ Решение: переименуйте все файлы и названия на английский, включая значки

   > **🚨 Важный момент Saturn-Builder.exe должен быть в английской папке!
   > При использовании в названии папок русских символов ничего работать не будет!**
   
   > "D:\FOLDER\SaturnBuilder_1.0.exe" ✅
   
   > "D:\пака на русском\SaturnBuilder_1.0.exe" ❌

## 🛠️ What It Needs / Что использует

Saturn-Builder downloads these tools automatically:
- **Node.js**: Helps run the app-making process.
- **JDK 17**: A tool to prepare your app for Android.
- **Android SDK**: Tools to build Android apps.
- **Gradle**: Helps put everything together.
- **Cordova CLI**: Makes apps from web projects.

❗You’ll need about 1 GB of space for all this❗

## 📬 Contact Us / Связь со мной (или нет)

- **GitHub**: [@EwenLoy](https://github.com/EwenLoy)
- **Email**: ewenloy@gmail.com
- **Youtube**: [@EwenLoy](https://www.youtube.com/@EwenLoy)
- **Telegram**: [SaturnBuilder](https://t.me/saturnbuilder)
- **Facebook**: Soon
- **Discord**: Soon
- **X (Twitter)**: [EwenLoy](https://x.com/EwenLoy)


## 💰 Buy Me a Coffee / ☕ Поддержите школьника:)
<div align="left"><img width="246" height="246" alt="qr-code" src="https://github.com/user-attachments/assets/23c8c13a-10dd-4507-b84b-8ea11071c769" />
   
Support Saturn-Builder! Scan the QR code or click below to buy me a coffee:
[<a href="https://www.donationalerts.com/r/ewenloy">Buy Me a Coffee</a>](https://www.donationalerts.com/r/ewenloy)

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=EwenLoy/Saturn-Builder&type=Date)](https://www.star-history.com/#EwenLoy/Saturn-Builder&Date)

## 📜 License

This project uses the MIT License. Check [LICENSE](LICENSE) for more info.

## 🔍 Search Keywords
- Construct 3 to APK
- Cordova APK builder
- Convert HTML5 to Android
- No code Android builder
- Construct 3 export Android

