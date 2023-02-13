using ConsoleApp1;
using System;

static class Menu
{
    public static void startMenu()
    {
        Console.WriteLine("\n1) Сравнение чисел");
        Console.WriteLine("2) Парсинг JSON");
        Console.WriteLine("3) Запрос http к интернет-ресурсу");
        Console.WriteLine("0) Выход\n");

        String menu = Console.ReadLine();

        while (true)
            switch (menu)
            {

                case "1":
                  
                    Console.WriteLine("\n\nВыбран пункт\"1) Сравнение чисел\", (0)Выход в меню");
                    Console.WriteLine("Введите два числа через пробел");

                    String str = Console.ReadLine();
                    if (str.Equals("0"))
                        startMenu(); 

                    var stringNumbers = str.Split(" ");

                    double numericValue1;
                    double numericValue2;

                    if (!stringNumbers.Length.Equals(2))
                    {
                        errorWrite("ERROR: Количество чисел меньше заялвенного");
                    
                        if (!double.TryParse(stringNumbers[0], out numericValue1))
                        {
                            errorWrite("ERROR: " + stringNumbers[0] + " Не является числом");
                            break;
                        }
                        if (!double.TryParse(stringNumbers[1], out numericValue2))
                        {
                            errorWrite("ERROR: " + stringNumbers[1] + " Не является числом");
                            break;
                        }
                    }

                    numericValue1 = Convert.ToDouble(stringNumbers[0]);
                    numericValue2 = Convert.ToDouble(stringNumbers[1]);

                    NumbernComparison.comparison(numericValue1, numericValue2);

                    break;
                case "2":
                    //
                    break;
                case "3":
                    //
                    break;
                case "0":
                    Environment.Exit(0);
                    break;
            }


        //	1) Необходимо написать консольную программу, где пользователь будет вводить с клавиатуры 2 числа.Числа будут сравниваться с последующим выводом в консоль результата этого сравнения(равны ли значения, а если нет, то какое число больше/меньше).
        //2) Разобрать json файл в массив и перебрать циклом
        //3) Обратиться к любому адресу в интернете, совершив http запрос
    }
    public static void errorWrite(string errorStr)
    {
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine(errorStr);
        Console.ResetColor();
    }   
    
    public static void resultWrite(string str)
    {
        Console.ForegroundColor = ConsoleColor.Green;
        Console.Write(str);
        Console.ResetColor();
    }
}
