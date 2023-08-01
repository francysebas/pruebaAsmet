import { Component } from '@angular/core';
import axios from 'axios';

@Component({
  selector: 'app-juzgado',
  templateUrl: './juzgado.component.html',
  styleUrls: ['./juzgado.component.css']
})
export class JuzgadoComponent {

  public obtJuzgados : any;
  public obtPersonas: any;
  public obtcaso: any;

  constructor(){

  }

  ngOnInit():void{
      this.getJuzgado();
      this.getPersona();
      this.getCaso();
  }

  getJuzgado(){
    const path = `http://127.0.0.1:8000/pruebaAsmet/juzgado/`
    axios.get(path).then((response)=>{
      this.obtJuzgados = response.data
      console.log("juzgados", this.obtJuzgados)
    })
    }

    getPersona(){
      const path = `http://127.0.0.1:8000/pruebaAsmet/persona/`
      axios.get(path).then((response)=>{
        this.obtPersonas = response.data
        console.log("persona", this.obtPersonas)
      })
      }

      getCaso(){
        const path = `http://127.0.0.1:8000/pruebaAsmet/caso/`
        axios.get(path).then((response)=>{
          this.obtcaso = response.data
          console.log("persona", this.obtcaso)
        })
        }

  }



