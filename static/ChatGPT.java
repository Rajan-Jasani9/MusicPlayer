package com.openai;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
public class ChatGPT {
	private final String apiKey;
	
	public ChatGPT(String apiKey){
		this.apiKey = apiKey;
	}
	
	public String complete(String input) throws Exception{
		String encodedInput = URLEncoder.encode(input,"UTF-8");
		String urlStr = "https://api.openai.com/v1/engines/davinci-codex/completions?prompt=" + encodedInput;
		URL url = new URL(urlStr);
		HttpURLConnection con = (HttpURLConnection) url.openConnection();
		con.setRequestMethod("POST");
		con.setRequestProperty("Authorization", "Bearer " + apiKey);
        con.setRequestProperty("Content-Type", "application/json");
        String requestBody = "{\"temperature\":0.5,\"max_tokens\":50}";

        con.setDoOutput(true);
        con.getOutputStream().write(requestBody.getBytes());
        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        StringBuilder response = new StringBuilder();
        String inputLine;
        while((inputLine = in.readLine()) != null) {
        	response.append(inputLine);
        }
        in.close();
        String[] splitResponse = response.toString().split("\"text\":\"");
        if(splitResponse.length > 1) return splitResponse[1].split("\",")[0];
        else return "";
	}
}
