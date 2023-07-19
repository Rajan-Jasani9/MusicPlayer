import com.openai.*;

public class virtual_assistant{
	public static void main(String[] args) throws Exception{
		ChatGPT chatGPT = new ChatGPT("<API-KEY>");
		String completedText = chatGPT.complete("Hello, GPT!");
		System.out.println(completedText);
	}
}
