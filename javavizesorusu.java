import java.util.Scanner;
	

	public class Main {
	    public static void main(String[] args) {
	        int i;
	        for (i=0; i < 20; i++) {
	            PeopleData pData = new PeopleData();
	            
	            // Öğrencinin ismini al.
	            System.out.print("İsim:");
	            Scanner name = new Scanner(System.in);
	            pData.studentName = name.next();
	            
	            // Matematik notunu al.
	            System.out.print("Matematik:");
	            Scanner math = new Scanner(System.in);
	            pData.Mathematics = math.nextInt();
	            
	            // Fen Bilgisi notunu al.
	            System.out.print("Fen:");
	            Scanner science = new Scanner(System.in);
	            pData.Science = science.nextInt();
	            
	            // Türkçe notunu al.
	            System.out.print("Türkçe:");
	            Scanner ling = new Scanner(System.in);
	            pData.Linguistics = ling.nextInt();
	            
	            // Ortalamanın eşik değerinin altında mı üstünde mi olduğu bilgisini al.
	            boolean state = Compute.isValid(pData.Mathematics, pData.Science, pData.Linguistics);
	            if (state) {
	                Letterize letter = new Letterize();
	                System.out.println(pData.studentName + ": " + 
	                    letter.getLetter(pData.Mathematics, pData.Science, pData.Linguistics));
	            }
	            else
	                // Çıktıyı stderr'e yazmak burada yanlış kaçar. Bu bir hata
	                // çıktısı değildir, dikkat! Olumsuz bir durum çıktısıdır.
	                // Bunu da standart çıktıya yönlendirmekte fayda var.
	                System.out.println(pData.studentName + ": " + "geçemedi");
	        }
	    }
	}
	

	class PeopleData {
	    int Mathematics;
	    int Science;
	    int Linguistics;
	    String studentName;
	}
	

	class Compute {
	    public static boolean isValid(int pointOne, int pointTwo, int pointThree) {
	        int average = (pointOne + pointTwo + pointThree) / 3;
	        return (average > 49) ? true : false;
	    }
	}
	

	class Letterize {
	    public String getLetter(int pointOne, int pointTwo, int pointThree) {
	        float average = (float)(pointOne + pointTwo + pointThree) / 3;
	        if (average >= 50 && average <= 70)
	            return "C";
	        if (average >= 71 && average <= 84)
	            return "B";
	        if (average >= 85 && average <= 100)
	            return "A";
	        return "F"; // Bunun anlamı ne? Hiçbir şey. Bir string döndürmekte fayda var.
	    }
	}