import openai

class ChatGPT:

    def __init__(self, model="gpt-3.5-turbo", completion_hparams=None):
        self.model = model
        self.completion_hparams = completion_hparams or {}
        self.history = []
        self._messages = []

    @property
    def messages(self):
        messages = [{"role": "system", "content": self._system}] + self._messages
        return messages
    
    def system(self, message, do_reset=True):
        if do_reset:
            self.reset()
        self._system = message

    def user(self, message):
        self._messages.append({"role": "user", "content": message})

    def assistant(self, message):
        self._messages.append({"role": "assistant", "content": message})

    def reset(self):
        self._messages = []

    def _make_completion(self, messages):
        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            **self.completion_hparams
        )
        self.history.append((messages, completion))
        return completion
    
    def call(self):
        completion = self._make_completion(self.messages)
        return completion["choices"][0]["message"]["content"].strip()
    
    def chat(self, message, replace_last=False):
        if replace_last:
            self._messages = self._messages[:-2]

        self.user(message)
        response = self.call()
        self.assistant(response)
        return response