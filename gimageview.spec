Summary:	Graphic Viewer
Summary(pl):	Przegl±darka plikow graficznych 
Name:		gimageview
Version:	0.2.1
Release:	1
License:	GPL
Group:		Applications/Multimedia
URL:		http://www.homa.ne.jp/~ashie/gimageview/
Source0:	http://west.dl.sourceforge.net/sourceforge/gtkmmviewer/%{name}-%{version}.tar.gz
Requires:	glib >= 1.2.6
Requires:  	gtk+ >= 1.2.6
Requires:	imlib >= 1.9
BuildRequires:	gtk+-devel 
BuildRequires:  imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GImageView is a GTK+ based image viewer. It support tabbed browsing,
thumbnail table views, directory tree views, drag and drop, reading
thumbnail cache of other famous image viewers, and flexible user
interface.

%description -l pl


%prep
%{__rm} -rf $RPM_BUILD_ROOT

%setup -q

%build
CFLAGS="%{rpmcflags}" export CFLAGS
%configure2_13 --prefix=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix}

gzip -9nf ABOUT-NLS AUTHORS  ChangeLog  README TIPS
%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gimv
%{_datadir}/gimageview/pixmaps/default/*.xpm
%{_datadir}/locale/*/LC_MESSAGES/gimageview.mo
 %{_libdir}/gimageview/*/*.so
