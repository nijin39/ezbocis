ezadmin Project
=======

[TOC]

stack
-------
 - psutil
 - python 3.5
 - apache kafka
 - mongo db
 - python flask
 - apache kafka
 - mongodb
 - web socket
 - bootstrap
 - graylog 참조
 - dashboard grafana 시계열 데이터
 - elasticsearch
 - Log aggregator 
  - Fluntd
  - Apahe Flume
  - GrayLog
 - ORM(FLASK SQLAlchemy)
 (기본적인 쿼리는 ORM을 사용하여 개발하도록 함.)
 - Prometheus : Grafana + Log aggregation  안이쁘지만.....
   - DEMO :  http://demo.robustperception.io:9090/graph
Function
-------

 - System monitoring
 - Event logging
 - Security Audit
 - System Automation(remote excution)
 - Port scanner 
 - SW discovery
 - Realtime Graph
 - Datacenter Management 
 - Packaging Easy Install
 - RDB & NOSQL 
     > 시계열 데이터는 NOSSQL에 RDB DATA는 mysql에 담도록 한다.
     
Detail Feature
-------
### Common Function

 - Logging 
 - ACL 
 - Remote Agent Upgrade
 - Performance Limit
 - Agent
  - Install Script
  - Comminication Test
  - Unique Key Generator
  - Test Locally 
  - Install through Internet
  - Security Layer Communication(option)
  - Excute Log

###Inventory Management

추후 CMDB로 관리해야 하며 프로젝트 시작에는 이력을 남기지 않고, 나중에는 변경에 대한 이력을 남겨야 한다.

  - HOSTNAME
  - IP(Each NIC)
  - VENDOR
  - MODEL
  - MANAGER(option)
  - OS Version
  - CPU / MEMORY 
  - DISK SIZE
  - CUSTOMER(option)

### System Monitoring

python psutil을 기준으로 확인할 수 있는 항목들을 기술한다.

#### Monitoring Inventory
 - CPU
  - cpu time / cpu percent / cpu stat  
 - Memory
   - usage 
     - total
     - available
     - percent
     - used
     - free
    - swap
     - total
     - used
     - free
     - percent
     - sin
     - sout
 - Disk
   - partitions
   - usage 
   - disk io count
     - read_count
     - write_count
     - read_bytes
     - write_bytes
 - Process
 - Network
   - Net io count
     - bytes_sent
     - bytes_recv
     - packets_sent
     - packets_recv
     - errin
     - errout
     - dropin
     - dropout  
   - Network connection 
   - Network NIC
   - Network Stat
     - isup
     - duplex
     - speed
     - mtu 
 - Inventory
   - Last boot
   - User
   - CPU COUNT 
   - MODEL
   - VENDOR
   - OS VERSION
 - SW discovery 

#### Monitoring Function
 - 임계치 관련 기능은 추후에 만듬
 - 항목들에 대한 표시만 만들
 - 항목들은 기본적으로 Dashboard 형태로 한대씩 표시
 - 데이터의 표시는 TEXT로 표시되고 추후 임계치 초과식 색으로 표시
 - 항목들에 대한 그래프 표시(한대당)
 - 여러대의 성능을 그래프로 볼수 있도록 표시(web socket)
 - 시계열 데이터의 경우는 선택해서 그래프를 표시할 수 있도록 준비
   (해당 DATA 표시는 Grafana를 검토해 볼것)
 - 서버별 임계치 템플릿 기능을 추가해야 함.

### Event Logging

  - 이벤트도 가능한 PYTHON을 이용하여 KFAKF로 수집하도록 한다.
     (https://github.com/leandrosilva/klogd)
     이것이 안될 것 같으면 Flume-kafka를 사용하도록 한다.
  - 로그는 시간 인터벌 별로 카운드가 되면 좋을 것 같다. 
  - 사용자가 특정 이벤드에 대해서 필터링을 할 수 있어야 한다.
  - 또한 특정 이벤트를 무시할 수도 있어야 한다.
  - 이벤트가 비정상적인 상황으로 증가할 때도 대처할 수 있어야 한다.
  - 이벤트 레벨별로 표시가 다르게 되어야 한다.

### Audit

  - 사용자가 사용하기 쉬워야 하며 배포되는 보안 정책들을 사용할 수 있어야 함.
  - lynis등을 이용하여 쉽게 만들어야 한다.(혹은 만들어?)
  - Audit에 대한 통합 DASHBOARD가 마련이 되야 한다.
  - 추후 결재 연동 가능성?
  - uncomflient한 정책에 대해서 바로 적용을 할 수 있어야 한다.
  - 여러대 서버에 실행이 가능해야 한다.
  - 주기적으로 수준에 대한 관리가 가능해야 한다.
  - 기존의 수집 방법인 Apache Kafka와 연동이 되어야 한다.

### SYSTEM AUTOMATION

  - 장비를 운영/감사함에 있어서 필요한 스크립트를 저장할 수 있는 기술이 있어야 함.
  - 해당 스크립트를 특정 서버 혹은 서버 그룹에 실행이 가능해야 하며 실행부터 결과까지의 모든 과정에 걸쳐 이력이 남아야 한다.
  - 해당 스크립트는 실행함에 있어서 프로세스/메모리의 제한이 있어야 한다.
  - 스크립트는 해당 스크립트 파일을 서버에 복사하고 수행결과는 서버로 비동기 전송되어야 한다.
  - 전송되는 결과 파일의 크기는 제한이 없어야 한다.
  - 수행되는 과정은 마이스톤 단위로 현재 진행 사항이 표시가 되어야 한다.(psutil의 외부 명령어 모듈 사용 테스트)
  - 해당 스크립트는 서버에서 root 외에 특별한 계정으로 돌릴 수 있어야 한다.
  - 스크립트 수행 결과는 시계열 Data가 아니므로 해당 결과는 RDB에 담겨져야 한다.
 
### Port Scanner
  - 추후 해당 시스템 구축시 Agent는 포트스캐너를 이용하여 적용 범위를 산정한다.
  -  python-nmap을 활용하도록 한다.
  - 해당 대역의 대표 IP만 등록하여 장비의 유무를 검색하고 장비를 검색하여 Agent를 배포할 수 있도록 한다.

### Software Discovery
  - 1차 : 프로세서명으로 몇개의 중요 프로그램의 기동을 확인함.(tomcat/mysql/oracle/jboss/apache)
  - 2차 : 파일의 Finger Print를 활용하여 SW를 찾아내도록 함.
  - SW명을 찾아낼 뿐 아니라 기본적인 SW의 설정값도 가져와 감사 할수도 있도록 해야 한다.

### Realtime Graph
  - 시계열 DATA의 경우 nosql에 기본으로 저장하고 해당 저장된 DATA를 바로 표시해주는 오픈 소스를 활용한다. 
    - Grafana(www.grafana.org) - elasticsearch
    - Graphite(graphite.wikidoc.com)
  - 가능한 오픈소스를 사용하여 개발 기간을 줄임.
  - WEB Socket를 사용하여 빠르게 그래프를 표시함.

### Datacenter Management
  - 데이터센터에서 혹은 더 많은 대상을 관리하기 위해서 수집된 CMDB이외의 부가적인 정보들에 대해서도 관리할 수 있도록 DB를 구성해야 한다.
    - 관리자(정), 관리자(부)
    - Datacenter 위치
    - 그외 추가될 수도 있는 정보들

### ETC
  - Packaging : Python의 경우 easy_install로 패키징 한다.
  - 시계열 데이터의 경우 Nosql에 담는다 현재로는 elasticsearch / mongo
  - 로그 처리의 경우 Klogd을 사용한다.
  -  
> Written with [StackEdit](https://stackedit.io/).
