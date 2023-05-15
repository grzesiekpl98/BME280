# BME280

BME280 sensor connected with Raspberry Pi Pico W programmed in micropython and sending data to Thingspeak

Pod linkiem znajduje się projekt czujnika BME280 połączonego z Raspberry Pi Pico W za pomocą języka Micropython. W projekcie dane zebrane z czujnika są wysyłane na serwer chmurowy Thingspeak, wzorując się na moim projekcie konieczne jest dodanie pliku secrets.py, w którym znajdują się SSID oraz hasło do użytej sieci Wi-Fi oraz odpowiedniej biblioteki do czujnika BME280. Projekt potrzebuje także indywidualnego kodu API wykreowanego przez Thingspeak.
