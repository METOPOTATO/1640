import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { UsersComponent } from './users/users.component';
import { LoginFormComponent } from './login-form/login-form.component';
import { MyService} from './my.service'
import { AdminComponent } from './admin/admin.component';
import { StudentComponent } from './student/student.component';
import { TutorComponent } from './tutor/tutor.component';
import { AppComponent } from './app.component';
import { ForbiddenComponent } from './forbidden/forbidden.component';

const routes: Routes = [
  {path:'staff',component:AdminComponent,canActivate:[MyService] ,data:{role:['staff']} },
  {path:'student',component:StudentComponent,canActivate:[MyService] ,data:{role:['student']}},
  {path:'tutor',component:TutorComponent,canActivate:[MyService] ,data:{role:['tutor']}},
  {path:'list',component:UsersComponent,canActivate:[MyService]},
  {path:'login',component:LoginFormComponent},
  {path:'forbidden',component:ForbiddenComponent}
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
