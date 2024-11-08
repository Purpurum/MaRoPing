## <div align="center">О данном проекте📝</div>
<p>Данная система представляет собой решение, включающее в себя несколько нейросетей, обёрнутых в веб приложение, развёртывающихся в докере. Целью системы является детекция и распознавание номеров грузовых ж/д вагонов, для автоматизации учёта.
</p>

## <div align="center">Запуск🔮</div>
<p>
!Вам понядобятся веса, доступные по этой <a href="https://disk.yandex.ru/d/6kH-wY8P_AWxuQ">ссылке</a> после загрузки их необходимо положить по пути backend/modules/models!
</p>
<p>
Для запуска проекта необходимо установить докер на систему.
</p>

<p>
Все дальнейшие команды должны выполняться в корневой директории проекта(куда он был склонирован), где также находится файл docker-compose.yml.
</p>

<p>
После этого нужно собрать образ докера командой:
</p>
  
```bash
$ docker compose build
```

<p>
После завершения установки можно будет запустить решение командой:
</p>

```bash
$ docker compose up
```
</details>

<div align="center">
  <img src="https://i.ibb.co/hy55hb2/ch-ban.png" alt="banner2" border="0" /></a>
</div>

## <div align="center">Стэк технологий📑</div>
<div align="center">
  <a href="https://www.python.org/doc/"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></a>
  <a href="https://pytorch.org/docs/stable/index.html"><img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white"></a>
  <a href="https://opencv.github.io/cvat/docs/"><img src="https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white"></a>
  <br>
  <a href="https://github.com/ultralytics/ultralytics?tab=readme-ov-file"><img src="https://img.shields.io/badge/Ultralytics-YOLOv8-purple.svg"></a>
</div>

## <div align="center">О нашем решении📝</div>
<p>
Наше решение является десктопным приложением, подсчитывающим количество представителей каждого вида животных на изображении.
Это приложение должно повысить удобство и скорость обработки изображений, получаемых с автоматических фотоловушек, работая в автономном режиме на PC оператора, без доступа в интернет. 
</p>

## <div align="center">Быстрый старт🎢</div>

####  Запуск приложения

<p>
  Вам необходимо:<br>
  &ensp; 1. Установить Python версии не меньше 3.9<br>
  &ensp; 2. В папку по пути models скачать и поллжить веса с ссылки https://disk.yandex.ru/d/1UPerq9luRkfCg<br>
  &ensp; 3. В cmd "pip install -r requirements.txt"<br>
  &ensp; 4. Запустить MainUI.py(в cmd python mainUI.py)<br>
</p>

#### Как это работает?
<p>
  После запуска приложения, пользователь видит понятный и интуитивынй итерфейс. Сценарий использования приложения такой:<br>
  &ensp; 1. Запустив приложение пользователь нажимает на кнопку "Открыть", в открывшемся проводнике он выбирает папку содержащую папки фотоловушек.<br>
  &ensp; 2. После этого пользователь нажимает кнопку "Запуск", после чего начнётся процесс оценки данных.<br>
  &ensp; 3. После окончания процесса польхователь может нажать на кнопку "Сохранить", после чего можно будет выбрать куда нужно сохранить полученный csv файл.<br>
  &ensp; 3.1. Также пользователь может посмотреть отдельные результаты работы, нажав на изображение в проводнике в левой части приложения.
</p> 
 
</details>

## <div align="center">Детекция, классификация и определение времени📸</div>
<p>
  Данное решение содержит несколько модулей: детектор и классификатор и определитель времени.
  В качестве детектора ипользуется бесклассовая модель Yolov8n.
  В качестве классификаторов используется ResNet101.
</p>
<div align="center">

  #### Схема работы приложения
  <p>
    <img src="https://i.ibb.co/hcxt496/schema.png" border="0" width="70%" /></a>
  </p>
  <!--<img src="" width="500" height="500"/>-->
</div>

## <div align="center">Результат работы моделей🔮</div>

<div align="center">
<p>
  Качество работы моделей на основании обучающего набора данных:<br>
  &ensp; Детектор: <br>
  Точность - 88%<br>
  &ensp; Классификатор: <br>
  Точность - 89%<br>
  &ensp; Алгоритм поиска времени: <br>
  IoU - 91%
</p>
</div>
