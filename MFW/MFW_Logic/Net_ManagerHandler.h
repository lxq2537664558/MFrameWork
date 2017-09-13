#pragma once
#include "Singleton.h"
#include "NNTCPServerMgr.h"
#include "Net_Handler.h"
/*
������Ϣ�ַ�������
���ڣ����������յ���Ϣ�ַ�����Ӧ�Ĵ�����

*/
class Net_ManagerHandler :public MFW::Singleton<Net_ManagerHandler>, public NetClient_Handler
{
private:
	NNTCPNode* mServerNetNode;
	std::shared_ptr<NNTCPLinkNode> mServerSession;
public:
	Net_ManagerHandler();
	virtual void OnRead(std::shared_ptr<NNTCPLinkNode>  session, std::string data, NNTCPNode& netNode);
	virtual void OnConnected(std::shared_ptr<NNTCPLinkNode>  session, NNTCPNode& netNode);
	virtual void OnDisConnected(std::shared_ptr<NNTCPLinkNode>  session, NNTCPNode& netNode);
	virtual void OnTimered(uv_timer_t* handle);

};