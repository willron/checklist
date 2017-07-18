/**
 * Created by zxp on 17-7-18.
 */
var app = new Vue({
    el: '#app',
    data: {
        todos: 'Check List'
    },
    delimiters : ['[[', ']]']
});

var checklists = new Vue({
    el: '#checklists',
    data: {
        lists:[
            //                 {name: 'abcd'},
            // {name: 'abcd'},
            // {name: 'abcd'}

        ]
    },
    created: function () {
        self = this;
        axios.get('../checklistapi/').then(function(response){
            self.lists = response.data;
        }).catch(function (error) {
            console.log(error);
        });
    },
    delimiters : ['[[', ']]']
});

