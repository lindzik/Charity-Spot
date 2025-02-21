import {BrowserRouter as Router,Route,Routes} from 'react-router-dom';
import Navigation from './Navigation';

import {ClientLogin} from '@charity-spot/client/login';
import {Register} from '@charity-spot/client/registration';
import {Profile} from '@charity-spot/client/organisation-profile';
import {Home} from '@charity-spot/client/home';
import {ClientDonate} from '@charity-spot/client/donate';
import {ClientChat} from '@charity-spot/client/chat';
import {ClientScheduleDelivery} from '@charity-spot/client/schedule-delivery'
import {ClientItemRequest} from '@charity-spot/client/item-request'
import {ClientItemRequestResults} from '@charity-spot/client/item-request-results'
import {ClientChatHistory} from '@charity-spot/client/chat-history'
import {ClientDeliveryScheduleInfo} from '@charity-spot/client/delivery-schedule-info'
import {ClientNotification} from '@charity-spot/client/notification'

function App() {
  return (
    <div className="App">
      <Router>
      <Navigation/>
        <Routes>
          <Route path ="/" element = { <ClientLogin/>}/>
          <Route path = "/login" element = {<ClientLogin/>}/>
          <Route path = "/register" element ={<Register/>}/>
          <Route path = "/profile" element ={<Profile/>}/>
          <Route path = "/home" element ={<Home/>}/>
          <Route path = "/donate" element = {<ClientDonate/>}/>
          <Route path = "/chat" element = {<ClientChat/>}/>
          <Route path = "/scheduleDelivery" element = {<ClientScheduleDelivery/>}/>
          <Route path = "/itemRequest" element = {<ClientItemRequest/>}/>
          <Route path = "/itemRequestResults" element = {<ClientItemRequestResults/>}/>
          <Route path = "/chatSessions" element = {<ClientChatHistory/>}/>
          <Route path = "/deliverySchedule" element = {<ClientDeliveryScheduleInfo/>}/>
          <Route path = "/notifications" element = {<ClientNotification/>}/>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
