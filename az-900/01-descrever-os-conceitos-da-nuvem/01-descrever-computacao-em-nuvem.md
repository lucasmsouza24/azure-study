# Descrever a computação em nuvem

## Descrever os conceitos da nuvem

### Definir a computação em núvem

A computação em nuvem é a entrega de serviços de computação pela Internet

Serviços de núvem geralmente podem entregar:
- VMs
- Storage
- Database
- Network
- IoT
- ML
- IA

Diferente de uma infraestrutura de datacenter comum, a computação em núvem permite flexibilidade no investimento e no uso de recursos dependendo da demanda.

### Descrever o modelo de responsabilidade compartilhada

Em um datacenter local, a equipe é responsável por garantir toda a segurança física do datacenter, bem como toda a infraestrutura de software, atualização/patches de segurança do SO, etc.

Já no modelo de responsabilidade compartilhada, essas responsabilidades são divididas entre provedor de núvem e consumidor. 

Essa divisão depende do tipo de serviço de núvem, podendo ser de responsabilidade do provedor de núvem, do consumidor ou de ambos em alguns casos. Como demonstra a seguinte imagem:

![shared-responsibility-model](../../img/01-shared-responsibility-model.png)

> Os tipos de serviços em núvem serão detalhados posteriormente.

#### O que sempre fica com o usuário (consumidor da núvem)

- As informações e os dados armazenados na nuvem
- Dispositivos que têm permissão para se conectar à nuvem (celulares, computadores e assim por diante)
- As contas e identidades das pessoas, serviços e dispositivos em seu ambiente

#### O que o provedor sempre possui

- O datacenter físico
- A rede física
- Hosts físicos

#### O que depende do tipo de serviço

- Sistemas operacionais
- Controles de rede
- Aplicativos
- Identidade e acesso
- Infraestrutura

### Definir modelos de nuvem

Os modelos de nuvem definem o tipo de implantação de recursos de nuvem.

#### Nuvem privada

Uma nuvem privada fornece serviços semelhantes aos de uma nuvem pública, porém o data center é de uso exclusivo de uma única organização, podendo ser on‑premises ou hospedado por terceiros. Esse modelo normalmente tem maior custo e complexidade, mas oferece mais controle e opções de conformidade.

#### Nuvem pública

Uma nuvem pública é criada, controlada e mantida por um provedor terceirizado e seus serviços podem ser consumidos pelo público em geral. Os recursos podem se compartilhar fisicamente por meio de multi‑tenancy, com divisões lógicas entre os consumidores. Benefícios incluem economia de escala e o modelo pay‑as‑you‑go.

#### Nuvem híbrida

Uma nuvem híbrida integra nuvens públicas e privadas em um ambiente interconectado. Combina o controle e a segurança da nuvem privada com a flexibilidade e a redução de custos da nuvem pública. Permite posicionar dados e cargas de trabalho conforme requisitos de segurança, latência e custo.


| Nuvem pública | Nuvem privada | Nuvem híbrida |
| ------------- | ------------- | ------------- |
| Reduz necessidade de CAPEX para escalabilidade | Controle total sobre recursos e segurança | Maior flexibilidade na alocação de cargas |
| Aplicações podem ser provisionadas e desprovisionadas rapidamente | Dados e recursos dedicados a um único locatário | Você determina onde executar seus aplicativos |
| Modelo pay‑as‑you‑go: paga pelo que usa | Hardware e manutenção ficam sob responsabilidade da organização | Combina controle e flexibilidade; pode aumentar a complexidade operacional |
| O provedor gerencia infraestrutura física | Organização gerencia manutenção e atualizações de hardware | Balanceia custos, conformidade e performance conforme necessidade |

#### Multicloud

Multicloud é o uso de dois ou mais provedores de nuvem pública para combinar recursos, evitar vendor lock‑in ou aproveitar serviços especializados.

#### Azure Arc

Azure Arc é um conjunto de tecnologias que ajuda a gerenciar ambientes de nuvem — públicos (por exemplo, Azure), privados, híbridos e multicloud. Permite gerenciar servidores, clusters Kubernetes e serviços on‑premises e em outras nuvens com as ferramentas do Azure.

#### Solução VMware no Azure

A Solução VMware no Azure permite executar cargas de trabalho VMware no Azure com integração, migração e opções de escalabilidade.

