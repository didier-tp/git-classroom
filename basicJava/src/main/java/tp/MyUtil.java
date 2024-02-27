package tp;

import javax.swing.JOptionPane;

public class MyUtil {
	public static void display(String message){
		System.out.println(message);
	}
	
	public static void displayDlg(String message){
		if(message!null)
		 JOptionPane.showMessageDialog(null, message);
	}
}
