package com.example; 

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.options.UiAutomator2Options;
import org.junit.jupiter.api.*; // ← JUnit 5!
import org.openqa.selenium.By;
import java.io.File;

import java.net.MalformedURLException;
import java.net.URL;
import java.time.Duration;

public class NotesTest { // ← имя класса = имени файла

    private AndroidDriver driver;

    @BeforeEach
public void setUp() throws MalformedURLException {
    // Надёжный путь — APK лежит в корне проекта автотестов
    String appPath = new File("app-debug.apk").getAbsolutePath();

    UiAutomator2Options options = new UiAutomator2Options()
            .setApp(appPath)
            .setPlatformName("Android")
            .setAutomationName("UiAutomator2")
            .setDeviceName("emulator-5554")
            .setNoReset(true);

    driver = new AndroidDriver(new URL("http://127.0.0.1:4723"), options);
    driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
}
    @Test
public void testTapAddNoteButton() {
    // Найти поле ввода и ввести текст
    driver.findElement(By.id("com.example.tpolab7:id/editTextNote")).sendKeys("Test");
    System.out.println("📝 Текст 'Тестовая заметка' введён");

    // Нажимаем кнопку
    driver.findElement(By.id("com.example.tpolab7:id/buttonAddNote")).click();
    System.out.println("✅ Кнопка 'Добавить заметку' нажата!");

    // Добавляем паузу на 5 секунд, чтобы увидеть результат
    try {
        Thread.sleep(5000); // 5000 мс = 5 секунд
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
}

    @AfterEach
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}