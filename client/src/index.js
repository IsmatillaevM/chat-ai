const { createApp } = Vue

const App = createApp({

  data() {

    return {

      questionText: '',
      typeanswer: '',
      chatlist: [],
      history: []



    }

  },

  methods: {
    getAnswer() {
      if (this.questionText && this.typeanswer != '') {
        request('/getAnswer', 'POST', { question: this.questionText, typeanswer: this.typeanswer }).then(data => {

          this.chatlist.push({ question: this.questionText, answer: data.answer, bleau: data.bleau })

        })
      }
      else {
        alert('Please fill the question and select the type of answer ')
      }
    },

    saveChatDb() {

      request('/saveChatDb', 'POST', { chatlist: this.chatlist })

      alert('Chat saved successfully')
    }
  }

})

App.mount('#vueapp')

async function request(url, method, data) {

  try {
    const headers = {}
    let body
    if (data) {
      headers['Content-Type'] = 'application/json'
      body = JSON.stringify(data)
    }
    const response = await fetch('http://127.0.0.1:5000' + url, {
      method,
      headers,
      body
    })

    return await response.json()

  }
  catch (e) {
    console.warn('Error:', e.message)
  }
}
