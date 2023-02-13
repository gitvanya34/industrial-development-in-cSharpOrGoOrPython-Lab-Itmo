using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    public static class NumbernComparison
    {
        public static void comparison(double num1, double num2)
        {
            if (num1 > num2)
                Menu.resultWrite(num1 + " > " + num2);
            else if (num1 < num2)
                Menu.resultWrite(num1 + " < " + num2);
            else if (num1 == num2)
                Menu.resultWrite(num1 + " == " + num2);
            else { Menu.errorWrite("Неопознанная ошибка сравнения"); }
        }
    }
}
