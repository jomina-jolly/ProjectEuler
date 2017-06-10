
public class Calucator {
static int a;
static int b;

public int add(int x,int y){
	return(x+y);
}

public int substract(int x,int y){
	return(x-y);		
}

public int multiply(int x,int y){
	return(x*y);
}
public int divide(int x,int y){
	return(x/y);
}
	public static void main(String[] args) {
		a=10;
		b=20;
		Calucator c= new Calucator();
		System.out.println( c.add(a, b));
		
		System.out.println(c.substract(15, 10));
		
	}

}
