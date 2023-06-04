const { createApp } = Vue

const App = createApp({

  data() {

    return {

      history:[]



    }

  },

  methods: {
  
    getHistory(){

      request('/getHistory', 'GET').then(data => {
      
        this.history.push(data)
        
      
      })
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
