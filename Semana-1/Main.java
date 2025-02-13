public class Main {
    public static void main(String[] args) {
        System.out.println(sbt(2, 2));
        System.out.println(add(5, 5));
    }

    public static int sbt(int a, int b) {
        int c = 0;
        while (b < a) {
            c++;
            b++;
        }
        return c;
    }

    public static int add(int a, int b) {
        int c = b;
        while (a > 0) {
            a--;
            c++;
        }
        return c;
    }
}
