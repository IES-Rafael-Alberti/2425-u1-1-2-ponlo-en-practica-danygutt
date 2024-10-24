import java.util.Scanner;  

public class programaEnJava {  
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);  


        System.out.print("Como te llamas: ");
        String nombre = scanner.nextLine();


        String mensaje = "Hola, " + nombre + " este programa está hecho en el lenguaje de programación: java";
        System.out.println(mensaje);
    }
}
