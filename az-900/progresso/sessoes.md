# Diário de sessões AZ-900

Uma entrada por sessão de estudo (por dia). Os itens de cada quiz ficam em `questoes.csv`, e os números consolidados, em `PAINEL.md`.

## Antes de 20/08/2026

Sem registro detalhado. Foram estudados com resumo e quizzes (geralmente 5/5) os conceitos de nuvem, os componentes arquitetônicos do Azure (regiões, zonas, recursos, assinaturas, grupos de gerenciamento e hierarquia) e as opções de computação e de VM.

## S01 — 20/08/2026

- **Estudado:** opções de hospedagem de aplicativos (App Service, contêineres e VMs).
- **Quiz:** 5/5.

## S02 — 25/08/2026

- **Estudado:** rede virtual (VNet, sub-redes, emparelhamento, DNS do Azure, VPN e ExpressRoute), com uma explicação extra sobre o papel de cada recurso de rede.
- **Quizzes:** 4/5 e 5/5. O erro foi de leitura, sobre o DNS do Azure.
- **Decisão:** os quizzes passaram a ter dificuldade de nível de prova, com distratores vizinhos.

## S03 — 06/10/2026

Retomada depois de cerca de 6 semanas sem estudar. Rodadas diagnósticas para medir o que ficou.

- **Conceitos de nuvem:** 10/10, com dúvida só em nuvem privada.
- **Componentes arquitetônicos:** 9/10. Errou pares de regiões (confundiu com regiões soberanas) e teve dúvida em regiões soberanas e em assinatura como limite de cobrança.
- **Computação:** 8/10. Errou ACI (confundiu com App Service) e domínio de atualização, e acertou conjunto de disponibilidade por eliminação.
- **Mini-rodada dos pontos frágeis:** 6/6, todas com certeza.
- **Rede (emparelhamento vs VPN vs ExpressRoute):** 4/6. Errou site a site (não conhecia a diferença para ponto a site) e o failover do ExpressRoute com VPN.
- **Aprendizados:** quando o enunciado já descreve o serviço em uso e pergunta como superar uma limitação dele, a resposta costuma ser um serviço complementar. Os termos do Learn são "site a site" e "ponto a site".

## S04 — 07/10/2026

- **Estudado:** profundidade cobrada no requisito de rede e trade-off entre o isolamento do ExpressRoute e o failover com VPN.
- **Quiz de rede geral:** 10/10, mas com dúvida em zonas DNS privadas e em um gateway por VNet, e chute em VPN baseada em rota.
- **Decisão:** a régua de profundidade passou a separar o essencial (finalidade e diferença entre vizinhos) do detalhe do Learn (no máximo 1 a cada 5 questões).

## S05 — 08/10/2026

- **Estudado:** endpoints públicos e privados, além de prática com AKS privado e endpoints privados em serviços PaaS (fora da prova).
- **Quiz:** 5/5.

## S06 — 09/10/2026

- **Estudado:** comparação dos serviços de armazenamento. A diferença entre Arquivos e Blobs ficou clara com a ideia de "pasta de rede" vs "depósito de objetos".
- **Quiz:** 7/7.

## S07 — 10/10/2026

- **Estudado:** camadas de acesso do Armazenamento de Blobs; explicação de opções de redundância (LRS, ZRS, GRS, GZRS e variantes RA-).
- **Quizzes:** 6/6 em múltipla escolha e 5 de 6 itens na rodada com formatos da prova. O erro foi por distração com a ordem das alternativas.
- **Decisões:** os quizzes passaram a misturar os formatos da prova real (Sim/Não, completar a frase, associação e múltipla seleção). O progresso passou a ser registrado nesta pasta.
- **Redundância:** leu o Learn e revisou as anotações (faltava RA-GRS e RA-GZRS). As siglas ficaram claras ao ignorar o "RS" final e decodificar por peças (L, Z, G, RA-), com a regra "sem Z, a principal é local".
- **Quiz de redundância:** 14 de 14 itens, todos com certeza, em cinco formatos.
- **Quiz de redundância (2ª rodada):** 13 de 14. Errou com certeza que RA- só permite leitura na secundária (não gravação). Acertou com dúvida a questão de "menor custo", por achar que o custo poderia prevalecer sobre um requisito.
- **Próximo:** opções de conta de armazenamento e tipos de armazenamento.

## S16 — 19/10/2026

- **Quiz de Azure Arc (G10):** 11 de 11 + 2/2 bônus (a 2B tinha sido digitada errada e foi corrigida).
- **Bônus:** ACI firme; domínio de atualização certo com dúvida (frágil).
- **Estudado:** infraestrutura como código (G11): código em vez de configuração manual; scripts (CLI/PowerShell, imperativos) vs modelos declarativos (ARM em JSON, Bicep); repetível e idempotente.
- **Quiz de IaC (G11):** 10 de 10 + 2/2 bônus. Dúvida na questão de scripts de implantação por enunciado ambíguo: propriedades do recurso (tamanho e quantidade de discos) vão no modelo; etapas dentro da VM (instalar nginx) usam script de implantação. O raciocínio dele estava certo.
- **Bônus:** domínio de falha (frágil) recuperado; endpoint privado firme.
- **Estudado:** Azure Resource Manager (G12): serviço de implantação e gerenciamento, fluxo da requisição (autentica, autoriza, envia ao serviço), mesma API para todas as ferramentas, benefícios (grupo, consistência, dependências, RBAC nativo, tags).
- **Quiz do Azure Resource Manager (G12):** 11 de 11 + 2/2 bônus (camada fria; grupos de gerenciamento), tudo com certeza. Bloco de ferramentas de gerenciamento e implantação (G08–G12) fechado.
- **Estudado:** Assistente do Azure (G13): recomendações personalizadas em cinco categorias (confiabilidade, segurança, desempenho, excelência operacional, custo), notificações de novas recomendações, painel filtrável.
- **Quiz do Assistente do Azure (G13):** 10 de 10 + 2/2 bônus (grupos de recursos; Arquivos vs Blobs), tudo com certeza. Advisor vs Azure Monitor (erro do simulado) recuperado.
- **Estudado:** Integridade do Serviço do Azure (G14): três visões (Status do Azure global, Integridade do Serviço para os seus serviços e regiões, Integridade de Recursos por recurso), alertas, histórico, links de suporte.
- **Próximo:** quiz da Integridade do Serviço.

## S15 — 18/10/2026

- **Quiz de fatores de custo (G01):** 10 de 11 + 2/2 bônus, tudo com certeza. Errou reserva vs plano de economia na escolha única (VM fixa por 3 anos é reserva), mas acertou o mesmo contraste na associação.
- **Bônus:** acesso condicional vs Resource Manager firmou; emparelhamento (erro do simulado) recuperado.
- **Estudado:** calculadora de preços (G02): estimativa antes de implantar, nada é provisionado, calculadora de TCO desativada.
- **Quiz da calculadora de preços (G02):** 8 de 10 + 2/2 bônus. Errou com dúvida a camada de acesso na estimativa por nomenclatura (leu "camada de acesso" como permissão, não como access tier) e marcou "preços" em vez de TCO por desatenção.
- **Bônus:** rede virtual é IaaS (erro do simulado) recuperado; segurança e governança na nuvem certo com dúvida sobre DDoS.
- **Estudado:** Microsoft Cost Management (G03): análise de custo, alertas de custo (orçamento, crédito, cota de departamento) e orçamentos com automação.
- **Quiz de Cost Management (G03):** 11 de 11 + 4/4 bônus, tudo com certeza. Separou alerta de orçamento (80% do limite) de alerta de métrica do Azure Monitor (CPU acima de 80%). Na múltipla escolha, acertou com dúvida: confundiu o Cost Management (conjunto de ferramentas) com a análise de custo (uma funcionalidade dentro dele).
- **Bônus:** reserva para recurso fixo recuperada; segurança e governança na nuvem (DDoS) firmou.
- **Estudado:** tags (G04): metadados nome/valor, usos (custo, operações, segurança, governança, automação), não herdam, Azure Policy exige ou reaplica.
- **Quiz de tags (G04):** 11 de 11 + 2/2 bônus (nuvem híbrida; pares de regiões), tudo com certeza. Tag vs bloqueio vs Policy vs RBAC firme (erro do simulado recuperado). Bloco de custos (G01–G04) fechado.
- **Estudado:** Microsoft Purview (G05): governança, risco e conformidade de dados; descoberta, classificação e linhagem; risco e conformidade (Microsoft 365) vs governança unificada de dados.
- **Quiz de Purview (G05):** 10 de 11 + 2/2 bônus. Na múltipla escolha "escolha duas" marcou só uma alternativa (faltou "identificar onde estão os dados confidenciais").
- **Bônus:** camada de acesso na calculadora recuperada; App Service firme.
- **Segunda rodada de Purview:** 10 de 10 + 2/2 bônus, tudo com certeza. Governança unificada de dados recuperada; calculadora de TCO e Cost Management vs análise de custo recuperados. Lista de revisão zerada.
- **Estudado:** Azure Policy (G06): políticas e iniciativas, escopos e herança, avaliação de recursos existentes, correção automática, exceções; contraste com RBAC, bloqueio e tag.
- **Quiz de Azure Policy (G06):** 11 de 11 + 2/2 bônus (Entra Connect; modelo baseado em consumo), tudo com certeza. Policy vs RBAC vs bloqueio vs tag firme; Owner não ignora a política.
- **Segunda rodada de Azure Policy:** 11 de 11, tudo com certeza (redimensionamento avaliado, escopos, correção automática, definição/iniciativa/atribuição/exceção).
- **Bônus:** 1 de 2. Errou de novo os casos de uso do acesso condicional por interpretação do enunciado: marcou aplicativos aprovados para "notebooks registrados e em conformidade" (é dispositivos gerenciados). Quarto erro no tema, a maioria de leitura (app vs dispositivo).
- **Estudado:** bloqueios de recursos (G07): CanNotDelete vs ReadOnly, escopos (recurso, RG, assinatura) e herança, valem independentemente do RBAC, remover antes de alterar.
- **Quiz de bloqueios de recursos (G07):** 11 de 11 + 2/2 bônus, tudo com certeza. Os dois erros do simulado (tag para impedir exclusão; bloqueio em grupo de gerenciamento) recuperados. Casos de uso do acesso condicional recuperados com app e dispositivo no mesmo enunciado. Bloco G05–G07 fechado.
- **Estudado:** portal do Azure (G08): console web gráfico, dashboards, acessibilidade, presença em todos os datacenters, sem tempo de inatividade para manutenção; Copilot no Azure como assistente.
- **Quiz do portal do Azure (G08):** 10 de 10 + 2/2 bônus (assinaturas; tempo real vs assíncrona), tudo com certeza. Portal + Cloud Shell no Android (erro do simulado) recuperado.
- **Cloud Shell, CLI e PowerShell (G09):** revisão rápida a partir do simulado e da unidade do portal; quiz curto 7 de 7 + 1/1 bônus (nuvem pública), tudo com certeza.
- **Estudado:** Azure Arc (G10): estende o Resource Manager, a conformidade e o monitoramento a recursos fora do Azure (local e outras nuvens); servidores, Kubernetes, serviços de dados, SQL Server, VMs (prévia).
- **Próximo:** quiz de Azure Arc (feito na S16).

## S14 — 17/10/2026

- **Decisão:** Defender para Nuvem (A27) adiado; volta depois de ter mais base (governança e ferramentas).
- **Estudado:** fatores que afetam custos no Azure (tipo de recurso, consumo, manutenção, geografia, tipo de assinatura, Marketplace; reservas, plano de economia, Spot).
- **Avaliação prática oficial da Microsoft (madrugada de 18/10):** 86% (43 de 50) em 19 minutos. Nuvem 13/14, arquitetura 18/19, governança 12/17. Erros: VNet é IaaS (marcou PaaS); emparelhamento (marcou endereços de serviço); bloqueio vs tag; escopo de bloqueio (marcou grupo de gerenciamento); Cloud Shell no Android (marcou SSH); Assistente do Azure vs Azure Monitor; Azure Monitor vs Integridade do Serviço.
- **Próximo:** quiz de fatores de custo (G01); quizzes de bloqueios/Policy; depois ferramentas e monitoramento (G08–G15).

## S13 — 16/10/2026

- **Estudado:** defesa em profundidade (camadas física → dados; propósito de não depender de uma só barreira).
- **Quiz:** 11 de 11 no tema + 2/2 bônus (confiabilidade; recursos de VM), tudo com certeza.
- **Decisão:** skill de questões — rótulo “escolha única” (1 certa) vs “múltipla escolha” (várias); anti-padrão S/N/S e AB repetidos.
- **Resumo (sem quiz):** Microsoft Defender para Nuvem — postura CSPM, Avaliar/Proteger/Defender, Azure + híbrido (Arc) + multinuvem; quiz quando voltar.
- **Resumos (sem quiz):** custos G01–G04 (fatores, calculadora de preços, Cost Management, tags) e governança G05–G07 (Purview, Azure Policy, bloqueios de recursos).
- **Próximo:** quizzes de A27 e depois G01–G07 quando estiver em casa.

## S12 — 15/10/2026

- **Revisão de RBAC:** 11 de 11, tudo com certeza (herança, modelo aditivo, privilégio mínimo, Colaborador vs Proprietário, app fora do RBAC).
- **Bônus:** casos de uso do acesso condicional recuperados (aplicativos cliente aprovados).
- **Revisão de acesso condicional:** 11 de 11 no tema + 1/1 bônus RBAC. Casos de uso firmes. Quase marcou Resource Manager como imposição do acesso condicional (acertou AC com dúvida) — gap: CA é Entra; ARM impõe RBAC.
- **Decisão:** bônus de revisão passa a priorizar temas frágeis/antigos (repetição espaçada), nunca o mesmo tema da rodada principal.
- **Revisão de identidades externas:** 11 de 13 no tema + 2/2 bônus. Erros no Sim/Não: conexão direta B2B não cria guest no diretório; ID Externa para clientes é para apps próprios (não negar essa afirmação).
- **Drill B2B vs direct connect vs ID Externa:** 6 de 6, tudo com certeza (gap fechado).
- **Estudado:** Confiança Zero (verificar explicitamente, privilégio mínimo, assumir violação; perímetro vs Zero Trust).
- **Quiz de Confiança Zero:** 11 de 11 no tema + 2/2 bônus (Functions; datacenter), tudo com certeza.
- **Próximo:** defesa em profundidade (A26).

## S11 — 14/10/2026

- **Retenção de opções de migração (quiz gerado em S10):** 9 de 11. Errou com certeza que bancos de dados e apps web ficam fora do hub das Migrações para Azure (são ferramentas integradas) e inverteu os rótulos "tempo real" (Migrações para Azure) e "assíncrona" (Data Box).
- **Discussão:** "assíncrona" no Learn não é sobre velocidade; é sobre origem e destino nunca estarem conectados ao mesmo tempo (etapas desacopladas). Data Box = físico, offline, assíncrono.
- **Estudado:** métodos de autenticação (senha, SSO, MFA, sem senha: Windows Hello para Empresas, Microsoft Authenticator, chaves FIDO2).
- **Quiz de métodos de autenticação:** 12 de 12; dúvida só se o Microsoft Authenticator conta como sem senha (conta).
- **Bônus de revisão:** 3 de 3, todos com certeza. Recuperou política de grupo (Domain Services), ferramentas integradas das Migrações para Azure e Data Box assíncrono.
- **Estudado:** identidades externas (colaboração B2B, conexão direta B2B, ID Externa para clientes, revisões de acesso).
- **Quiz de identidades externas:** 10 de 11. Errou com dúvida que a ID Externa para clientes publica apps da Microsoft (exclui apps da Microsoft; é para SaaS e apps próprios).
- **Bônus de revisão:** 4 de 4 (Authenticator sem senha firmou; herança no nível da assinatura).
- **Estudado:** acesso condicional do Microsoft Entra (sinal, decisão, imposição; casos de uso).
- **Quiz de acesso condicional:** 9 de 11. Os dois erros foram a troca entre "aplicativos aprovados" e "bloquear fontes não confiáveis" na associação (provável troca de letras).
- **Bônus de revisão:** 2 de 2 (ID Externa para clientes recuperada; GRS).
- **Estudo de RBAC do Azure** (escopo, herança, modelo aditivo, Resource Manager, funções internas).
- **Quiz de RBAC:** 12 de 12, tudo com certeza.
- **Bônus de revisão:** 1 de 2. Errou de novo os casos de uso do acesso condicional por leitura (entendeu "app móvel" como dispositivo móvel); Domain Services certo.
- **Próximo:** revisar casos de uso do acesso condicional; depois Confiança Zero (A25).

## S10 — 13/10/2026

- **Sessão:** revisão de retenção de serviços de diretório (estudado na noite anterior), depois métodos de autenticação.
- **Retenção de serviços de diretório:** 10 de 11. O Proxy de Aplicativo ficou firme (2 de 2). Errou com certeza que o Entra ID aplica política de grupo sozinho (provável confusão com as políticas do Intune e do acesso condicional).

## S09 — 12/10/2026 (noite) / 13/10

- **Sessão:** revisão dos erros da mini-rodada de rede e computação, antes de começar identidade.
- **Quiz de revisão (gateway de VPN, VPN baseada em rota, availability set vs VMSS):** 11 de 11, todos com certeza. Os três temas que estavam a revisar foram recuperados.
- **Rodada de retenção (temas de 6 a 8/10):** 15 de 15, todos com certeza. Conceitos de nuvem, hierarquia, computação, regiões e endpoints seguem firmes depois de 6 dias.
- **Decisão:** revisão diária curta, inclusive nos dias de conteúdo novo.
- **Estudado:** serviços de diretório (Microsoft Entra ID, Microsoft Entra Connect e Microsoft Entra Domain Services).
- **Quiz de serviços de diretório (feito de propósito antes de aprofundar):** 7 de 10. Errou Domain Services vs AD DS em VMs (duas vezes) e a sincronização de uma direção do Domain Services. Causa raiz: não conhecia Active Directory, Kerberos e LDAP; explicação de base feita com analogias web (OIDC vs Kerberos).
- **Quiz de serviços de diretório (2ª rodada):** 11 de 11, todos com certeza. Domain Services vs AD DS em VMs e a sincronização de uma direção foram recuperados.
- **Quiz de serviços de diretório (3ª rodada):** 8 de 11. Superestimou o Entra Connect: escolheu-o para publicar apps locais (é o Proxy de Aplicativo), para NTLM (é o Domain Services) e como requisito do Domain Services em empresa sem AD local.
- **Rodada do papel do Entra Connect:** 5 de 6. A regra "sem AD local, sem Connect" firmou; errou de novo, com certeza, que o acesso a apps locais é do Proxy de Aplicativo. Mnemônico: "Connect leva gente, Proxy leva app".
- **Simulado de serviços de diretório (10 questões, nível prova):** 17 de 17 itens, todos com certeza, incluindo o Proxy de Aplicativo. A tabela de decisão ("palavras do mundo antigo" levam ao Domain Services; Connect leva gente, Proxy leva app) funcionou.
- **Próximo:** métodos de autenticação (SSO, MFA e acesso sem senha), com 1 item de Proxy de Aplicativo na revisão do dia seguinte.

## S08 — 11/10/2026

- **Estudado:** tipos de conta de armazenamento (uso geral v2 Standard e as três Premium), redundância suportada por tipo, nome exclusivo da conta e endpoints.
- **Prática (fora da prova):** criou uma conta uso geral v2 Standard com LRS e testou o acesso a blobs: contêiner privado só abre com token SAS; o público exige habilitar o acesso anônimo na conta e o nível Blob no contêiner.
- **Quiz de tipos de conta:** 12 de 12, todos com certeza. Dúvida conceitual: o que é NFS e a diferença entre Arquivos no uso geral v2 Standard e em compartilhamentos de arquivos Premium.
- **Quiz de tipos de conta (2ª rodada):** 12 de 13. Errou com dúvida que a conta é acessível por HTTP/HTTPS (achou que Arquivos seria só SMB ou NFS; todos os serviços têm API REST). Aprendeu o que são blobs de blocos, de acréscimo e de páginas.
- **Pendente:** resumo de tipos de conta para o Notion, com uma linha explicando que NFS é um protocolo de compartilhamento de arquivos como o SMB (nativo do Linux).
- **Estudado:** opções para mover arquivos (AzCopy, Gerenciador de Armazenamento do Azure, Sincronização de Arquivos do Azure).
- **Quiz de mover arquivos:** 11 de 11. Data Box acertado por eliminação (registrado com dúvida) e dúvida em substituir servidor com falha na Sincronização de Arquivos.
- **Quiz de mover arquivos (2ª rodada):** 11 de 11, todos com certeza. A ideia de "servidor local como cache" consolidou a questão de substituir servidor com falha.
- **Decisão:** alternativas das questões sempre em itens de lista separados, para facilitar a leitura.
- **Estudado:** opções de migração (Migrações para Azure e Azure Data Box).
- **Quiz de opções de migração:** 11 de 11, todos com certeza. Data Box, antes acertado por eliminação, ficou firme.
- **Marco:** todos os requisitos de armazenamento (A14 a A19) estudados.
- **Revisão geral de armazenamento (A14 a A19):** 15 de 15, todos com certeza, incluindo os temas que estavam a revisar (RA- só leitura, acesso por HTTPS) e frágeis (serviços por tipo de conta).
- **Mini-rodada de pendentes (rede, computação e nuvem):** 8 de 11. Recuperou VPN como failover do ExpressRoute, zonas DNS privadas e nuvem privada. Errou no chute um gateway de VPN por VNet e o gateway conectando vários locais, e confundiu conjunto de disponibilidade com escala automática (VMSS).
- **Próximo:** identidade, acesso e segurança (A20 a A27), começando pelo Microsoft Entra ID.
